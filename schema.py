#!/usr/bin/env python3

import json
import sys


def convert_field(jd, gfield):
    name = jd['f9'][gfield['F4_f1']]

    f2 = gfield['F4_f2']
    f3 = gfield['F4_f3']

    if f3 in [0, 1]:
        gtype = jd['f5'][f2]['F5_f1']
    elif f3 in [4, 5, 6]:
        gtype = jd['f9'][f2]

    if f3 in [1, 5]:
        gtype = '[{}]'.format(gtype)

    return {
        'name': name,
        'type': gtype,
    }


def convert_type(jd, gtype):
    name = gtype['F5_f1']

    if 'F5_f2' in gtype:
        primary_key = jd['f4'][gtype['F5_f2']]
        primary_key = convert_field(jd, primary_key)

    else:
        primary_key = None

    fields = []
    for field in gtype['F5_f3']:
        field = jd['f4'][field]
        field = convert_field(jd, field)
        fields.append(field)

    return {
        'name': name,
        'primary_key': primary_key,
        'fields': fields,
    }


def main(fin):
    fin = open(fin, 'rt')
    jd = json.load(fin)

    schema = []
    for gtype in jd['f5']:
        gtype = convert_type(jd, gtype)
        schema.append(gtype)

    json.dump(schema, sys.stdout)

    fin.close()


if __name__ == '__main__':
    main(sys.argv[1])
