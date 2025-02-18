-- Declare the protocol
game_proto = Proto("GameAc", "Game Action Protocol")

-- Define the fields
local f_type = ProtoField.uint8("gameac.type", "Type", base.HEX)
local f_length = ProtoField.uint16("gameac.length", "Length", base.DEC)
local f_data = ProtoField.string("gameac.data", "Game Data")

game_proto.fields = { f_type, f_length, f_data }

-- Dissector function
function game_proto.dissector(buffer, pinfo, tree)
    local buffer_len = buffer:len()
    
    -- Ensure minimal packet length
    if buffer_len < 3 then  
        tree:add_expert_info(PI_MALFORMED, PI_ERROR, "Packet too short for Game Action Protocol")
        return
    end

    local offset = 0
    local subtree = tree:add(game_proto, buffer(), "Game Actions Data")

    -- Read Type (1 byte)
    local game_type = buffer(offset, 1):uint()
    subtree:add(f_type, buffer(offset, 1))
    offset = offset + 1

    -- Read Length (2 bytes, Big-Endian)
    local game_length = buffer(offset, 2):uint()  -- Changed from `le_uint()` to `uint()`
    subtree:add(f_length, buffer(offset, 2))
    offset = offset + 2

    -- Validate length
    local remaining_bytes = buffer_len - offset
    
    -- Add a maximum expected length (e.g., 512 bytes) to avoid false errors
    if game_length > 512 then
        subtree:add_expert_info(PI_MALFORMED, PI_ERROR, "Unrealistic length field (" .. game_length .. " bytes, max expected: 512)")
        return
    end
    
    if game_length > remaining_bytes then
        subtree:add_expert_info(PI_MALFORMED, PI_ERROR, "Truncated game message (Expected " .. game_length .. " bytes, but only " .. remaining_bytes .. " available)")
        return
    end

    -- Read Data
    local game_data = buffer(offset, game_length):string()
    subtree:add(f_data, buffer(offset, game_length)):append_text(" (" .. game_data .. ")")
    
    pinfo.cols.protocol = "GameAc"
end

-- Register the dissector
udp_table = DissectorTable.get("udp.port")
udp_table:add(800, game_proto)
