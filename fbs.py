import struct


def decode_vt_at(data, offset):
    vt_len = get_short(data, offset)
    tbl_len = get_short(data, offset + 2)

    if (vt_len < 0) or (tbl_len < 0):
        raise Exception('Invalid virtual table')

    if (vt_len % 2):
        raise Exception('Invalid virtual table')

    vt_nrent = int(vt_len / 2)
    if vt_nrent < 3:
        raise Exception('Invalid virtual table')

    entries = struct.unpack('<' + 'h' * vt_nrent, data[offset: offset + vt_len])[2:]

    return {
        'vt_len': vt_len,
        'tbl_len': tbl_len,
        'entries': entries
    }


def deref_offset(data, offset, reverse=False):
    off = get_int(data, offset)

    if reverse:
        return offset - off
    
    else:
        return offset + off


def get_table_vt(data, offset):
    vt_offset = deref_offset(data, offset, True)
    return decode_vt_at(data, vt_offset)


def get_int(data, offset):
    return struct.unpack('<i', data[offset: offset + 4])[0]


def get_short(data, offset):
    return struct.unpack('<h', data[offset: offset + 2])[0]


def get_vector_el(data, offset, el_type, n):
    vector_len = get_int(data, offset)
    vector_base = offset + 4

    if n >= vector_len:
        raise Exception('Invalid offset or vector')

    el_size = types[el_type]['size']

    return vector_base + n * el_size


def get_table_field(data, offset, n):
    vt = get_table_vt(data, offset)
    e_off = vt['entries'][n]

    if e_off == 0:
        return None

    return offset + e_off


def hex_dump(buf):
    ret = ''

    for e in buf:
        ret += ' {:02X}'.format(e)

    return ret


types = {
    'int': {
        'decode': get_int,
        'size': 4
    },
    'short': {
        'decode': get_short,
        'size': 2
    }
}
