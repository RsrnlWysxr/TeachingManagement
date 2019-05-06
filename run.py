# -*- encoding: utf-8 -*-
from app import app
import www
import sys


def main():
    app.run(host='0.0.0.0', debug=True)


if __name__ == "__main__":
    sys.exit(main())
