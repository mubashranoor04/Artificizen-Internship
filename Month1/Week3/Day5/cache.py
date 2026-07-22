"""
Simple in-memory cache using MD5 hashes.
"""

import hashlib

cache = {}


def get_cache_key(query: str) -> str:
    return hashlib.md5(query.lower().strip().encode()).hexdigest()


def get_cached_answer(query):

    key = get_cache_key(query)

    if key in cache:
        print("CACHE HIT")
        return cache[key]

    print("CACHE MISS")
    return None


def save_to_cache(query, answer, sources):

    key = get_cache_key(query)

    cache[key] = {
        "answer": answer,
        "sources": sources,
    }