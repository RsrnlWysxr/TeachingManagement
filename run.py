# -*- encoding: utf-8 -*-
from app import create_app
import sys


def main():
    app = create_app()
    app.run(host='0.0.0.0', debug=True)


if __name__ == "__main__":
    sys.exit(main())
