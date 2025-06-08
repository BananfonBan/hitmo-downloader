import asyncio
from hd.cli import parse_arguments
from hd.app import app


def main():
    args = parse_arguments()
    asyncio.run(app(args.urls, args.output, args.yes, args.limit))

if __name__ == "__main__":
    main()
