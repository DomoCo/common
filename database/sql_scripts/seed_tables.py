#!/usr/bin/env python

import sys

from engine import engine
from seeders.base_seeder import BaseSeeder
import seeders.template
import seeders.game_engine


if __name__ == '__main__':
    raw_seeders = BaseSeeder.__subclasses__()
    seeders = {}
    for raw_seeder in raw_seeders:
        seeders[raw_seeder.__name__] = raw_seeder
    session = engine.get_session()
    if len(sys.argv) <= 1:
        for seeder in seeders.values():
            seeder(session).seed()
    else:
        if sys.argv[1] in seeders:
            seeders[sys.argv[1]](session).seed()
        else:
            print('Invalid seeder given must be one of: %s' % ' '.join(seeders.keys()))
            sys.exit(1)
    session.commit()
