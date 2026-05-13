"""Compatibility wrapper for the LogicRAG iFinD data plugin.

The original demo mixed helper functions with executable examples and referred
to undefined objects such as IFINDHttpClient/QueryKeys.  The real implementation
now lives in ifind_data_plugin.py.  This file keeps the old module name usable
while avoiding side effects on import.
"""

from ifind_data_plugin import (
    DEFAULT_FUTURES_INDICATORS,
    DEFAULT_NONFERROUS_CODES,
    DEFAULT_STOCK_INDICATORS,
    FuturesDomainDictionary,
    IFINDDataClient,
    RequiredMaterialResolver,
    build_arg_parser,
    parse_query_date,
    run_data_plugin,
)


# Backward-compatible alias for older code that expected IFINDHttpClient.
IFINDHttpClient = IFINDDataClient


def main() -> None:
    parser = build_arg_parser()
    args = parser.parse_args()
    result = run_data_plugin(args)
    print("LogicRAG iFinD data plugin completed.")
    print(f"- query_date: {result['query_date']}")
    print(f"- spec_count: {result['spec_count']}")
    print(f"- flat_csv: {result['outputs']['flat_csv']}")
    print(f"- data_bindings: {result['outputs']['data_bindings']}")
    if args.dry_run:
        print("- dry_run: iFinD API was not called")


if __name__ == "__main__":
    main()
