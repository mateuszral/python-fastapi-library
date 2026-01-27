from fastapi import FastAPI

app = FastAPI()

books = [
    {
        "isbn": 9780000000001,
        "title": "The Silent Horizon",
        "author": "Ava Thompson",
        "pages": 312,
        "release_date": "2012-05-14"
    },
    {
        "isbn": 9780000000002,
        "title": "Echoes of Tomorrow",
        "author": "Liam Carter",
        "pages": 428,
        "release_date": "2015-09-22"
    },
    {
        "isbn": 9780000000003,
        "title": "Midnight Algorithms",
        "author": "Noah Reynolds",
        "pages": 256,
        "release_date": "2019-01-10"
    },
    {
        "isbn": 9780000000004,
        "title": "The Last Ember",
        "author": "Isabella Moore",
        "pages": 389,
        "release_date": "2017-11-03"
    },
    {
        "isbn": 9780000000005,
        "title": "Fragments of Blue",
        "author": "Ethan Walker",
        "pages": 301,
        "release_date": "2014-06-18"
    },
    {
        "isbn": 9780000000006,
        "title": "Clockwork Skies",
        "author": "Sophia Bennett",
        "pages": 472,
        "release_date": "2018-03-27"
    },
    {
        "isbn": 9780000000007,
        "title": "The Paper Kingdom",
        "author": "Oliver Hayes",
        "pages": 344,
        "release_date": "2013-08-09"
    },
    {
        "isbn": 9780000000008,
        "title": "Code of Ashes",
        "author": "Mia Collins",
        "pages": 295,
        "release_date": "2020-10-30"
    },
    {
        "isbn": 9780000000009,
        "title": "Winds Beyond the Map",
        "author": "Lucas Martin",
        "pages": 411,
        "release_date": "2016-04-12"
    },
    {
        "isbn": 9780000000010,
        "title": "Neon Valleys",
        "author": "Harper Scott",
        "pages": 367,
        "release_date": "2021-07-01"
    },
    {
        "isbn": 9780000000011,
        "title": "The Iron Orchard",
        "author": "Benjamin Lewis",
        "pages": 522,
        "release_date": "2011-02-25"
    },
    {
        "isbn": 9780000000012,
        "title": "A Measure of Stars",
        "author": "Emily Young",
        "pages": 284,
        "release_date": "2014-12-05"
    },
    {
        "isbn": 9780000000013,
        "title": "Synthetic Dawn",
        "author": "Daniel Kim",
        "pages": 338,
        "release_date": "2019-09-17"
    },
    {
        "isbn": 9780000000014,
        "title": "The Forgotten Signal",
        "author": "Chloe Ramirez",
        "pages": 406,
        "release_date": "2016-06-29"
    },
    {
        "isbn": 9780000000015,
        "title": "Beneath the Static",
        "author": "James Patel",
        "pages": 261,
        "release_date": "2018-01-19"
    },
    {
        "isbn": 9780000000016,
        "title": "Glassboun",
        "author": "Natalie Brooks",
        "pages": 354,
        "release_date": "2015-10-02"
    },
    {
        "isbn": 9780000000017,
        "title": "The Long Compile",
        "author": "Ryan Foster",
        "pages": 487,
        "release_date": "2022-04-14"
    },
    {
        "isbn": 9780000000018,
        "title": "Harbor of Dust",
        "author": "Victoria Nguyen",
        "pages": 319,
        "release_date": "2013-03-08"
    },
    {
        "isbn": 9780000000019,
        "title": "Anatomy of a Loop",
        "author": "Andrew Miller",
        "pages": 298,
        "release_date": "2020-02-11"
    },
    {
        "isbn": 9780000000020,
        "title": "The Copper Night",
        "author": "Zoe Parker",
        "pages": 445,
        "release_date": "2017-09-15"
    },
    {
        "isbn": 9780000000021,
        "title": "Parallel Weather",
        "author": "Jonathan Reed",
        "pages": 333,
        "release_date": "2014-05-20"
    },
    {
        "isbn": 9780000000022,
        "title": "The Broken Index",
        "author": "Hannah Coleman",
        "pages": 376,
        "release_date": "2019-11-08"
    },
    {
        "isbn": 9780000000023,
        "title": "Rust & Starlight",
        "author": "Aaron Price",
        "pages": 402,
        "release_date": "2016-01-26"
    },
    {
        "isbn": 9780000000024,
        "title": "Latency",
        "author": "Priya Desai",
        "pages": 287,
        "release_date": "2021-03-03"
    },
    {
        "isbn": 9780000000025,
        "title": "The Seventh Variable",
        "author": "Michael O'Connor",
        "pages": 469,
        "release_date": "2018-07-12"
    },
    {
        "isbn": 9780000000026,
        "title": "After the Overflow",
        "author": "Lauren Evans",
        "pages": 341,
        "release_date": "2015-02-06"
    },
    {
        "isbn": 9780000000027,
        "title": "Cold Start City",
        "author": "Kevin Zhao",
        "pages": 358,
        "release_date": "2022-09-09"
    },
    {
        "isbn": 9780000000028,
        "title": "The Hidden Stack",
        "author": "Rebecca Morgan",
        "pages": 291,
        "release_date": "2017-04-21"
    },
    {
        "isbn": 9780000000029,
        "title": "Signals at Dusk",
        "author": "Thomas Anderson",
        "pages": 414,
        "release_date": "2013-10-18"
    },
    {
        "isbn": 9780000000030,
        "title": "Inheritance Tree",
        "author": "Melissa Wright",
        "pages": 379,
        "release_date": "2016-12-02"
    },
    {
        "isbn": 9780000000031,
        "title": "The Floating Constant",
        "author": "Patrick Sullivan",
        "pages": 266,
        "release_date": "2020-06-05"
    },
    {
        "isbn": 9780000000032,
        "title": "Redshift Harbor",
        "author": "Alyssa Turner",
        "pages": 392,
        "release_date": "2018-10-23"
    },
    {
        "isbn": 9780000000033,
        "title": "Cache Miss",
        "author": "Brandon Lee",
        "pages": 243,
        "release_date": "2021-01-15"
    },
    {
        "isbn": 9780000000034,
        "title": "The Violet Archive",
        "author": "Samantha Green",
        "pages": 456,
        "release_date": "2014-09-11"
    },
    {
        "isbn": 9780000000035,
        "title": "Before the Merge",
        "author": "Chris Adams",
        "pages": 328,
        "release_date": "2019-08-28"
    },
    {
        "isbn": 9780000000036,
        "title": "The Golden Exception",
        "author": "Nina Lopez",
        "pages": 371,
        "release_date": "2017-05-19"
    },
    {
        "isbn": 9780000000037,
        "title": "Silent Functions",
        "author": "Jason Murphy",
        "pages": 259,
        "release_date": "2012-11-30"
    },
    {
        "isbn": 9780000000038,
        "title": "Beyond the Endpoint",
        "author": "Katherine Hill",
        "pages": 404,
        "release_date": "2022-02-22"
    },
    {
        "isbn": 9780000000039,
        "title": "A Gentle Overflow",
        "author": "Robert King",
        "pages": 347,
        "release_date": "2015-07-07"
    },
    {
        "isbn": 9780000000040,
        "title": "The Amber Protocol",
        "author": "Olivia Perez",
        "pages": 421,
        "release_date": "2018-12-14"
    },
    {
        "isbn": 9780000000041,
        "title": "Winter in Null Space",
        "author": "Steven Baker",
        "pages": 388,
        "release_date": "2016-02-16"
    },
    {
        "isbn": 9780000000042,
        "title": "Fault Lines",
        "author": "Rachel Howard",
        "pages": 273,
        "release_date": "2013-06-01"
    },
    {
        "isbn": 9780000000043,
        "title": "The Recursive Sea",
        "author": "David Nguyen",
        "pages": 462,
        "release_date": "2020-11-19"
    },
    {
        "isbn": 9780000000044,
        "title": "Static Gardens",
        "author": "Emma Wilson",
        "pages": 316,
        "release_date": "2014-04-04"
    },
    {
        "isbn": 9780000000045,
        "title": "Late Binding",
        "author": "Paul Roberts",
        "pages": 299,
        "release_date": "2019-03-26"
    },
    {
        "isbn": 9780000000046,
        "title": "The Last Semaphore",
        "author": "Linda Martinez",
        "pages": 437,
        "release_date": "2017-08-08"
    },
    {
        "isbn": 9780000000047,
        "title": "Underflow",
        "author": "Mark Thompson",
        "pages": 252,
        "release_date": "2021-12-03"
    },
    {
        "isbn": 9780000000048,
        "title": "A Map of Quiet Things",
        "author": "Julia Anderson",
        "pages": 365,
        "release_date": "2015-01-13"
    },
    {
        "isbn": 9780000000049,
        "title": "The Soft Delete",
        "author": "Alex Rivera",
        "pages": 281,
        "release_date": "2022-06-17"
    },
    {
        "isbn": 9780000000050,
        "title": "Memory Leak",
        "author": "Taylor Scott",
        "pages": 409,
        "release_date": "2018-09-04"
    }
]


@app.get("/")
def read_root():
    return "Welcome to library"

@app.get("/books")
def get_all_books(limit: int = 10, offset: int = 0) -> list:
    return books[offset:limit]

@app.get("/books/{book_id}")
def get_book(book_id: int) -> dict | bool:
    book = next((item for item in books if item["isbn"] == book_id), False)
    return book
