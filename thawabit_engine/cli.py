"""Simple CLI scaffold for thawabit_engine (lightweight)
"""
import argparse
import sqlite3
from pathlib import Path
from thawabit_engine.engine import ThawabitEngine

DEFAULT_DB = 'thawabit.db'

def main():
    psr = argparse.ArgumentParser(prog='thawabit')
    sub = psr.add_subparsers(dest='cmd')

    add = sub.add_parser('add-claim')
    add.add_argument('--id', type=int, required=True)
    add.add_argument('--domain', required=True)
    add.add_argument('--text', required=True)

    setst = sub.add_parser('set-status')
    setst.add_argument('--claim-id', type=int, required=True)
    setst.add_argument('--status', required=True)
    setst.add_argument('--reviewer')
    setst.add_argument('--reason')

    args = psr.parse_args()
    dbpath = Path(DEFAULT_DB)
    conn = sqlite3.connect(str(dbpath))
    engine = ThawabitEngine(conn)

    # try to apply schema if missing
    import pkgutil, io
    schema_bytes = pkgutil.get_data(__package__, 'schema.sql')
    if schema_bytes:
        engine.apply_schema(schema_bytes.decode())

    if args.cmd == 'add-claim':
        engine.add_claim(args.id, args.domain, args.text)
        print(f'claim {args.id} added')
    elif args.cmd == 'set-status':
        engine.set_status(args.claim_id, args.status, args.reviewer, args.reason)
        print('status set')
    else:
        psr.print_help()

if __name__ == '__main__':
    main()
