import cProfile
import io
import pstats


def profile(func):
    def wrap(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable(subcalls=True)
        result = func(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return result

    return wrap


def read_movies(src):
    with open(src) as fd:
        return fd.read().splitlines()

@profile
def is_duplicate(needle, haystack):
    for movie in haystack:
        if needle.lower() == movie.lower():
            return True
    return False



def find_duplicate_movies(src='movies.txt'):
    movies = read_movies(src)
    duplicates = []
    while movies:
        movie = movies.pop()
        if is_duplicate(movie, movies):
            duplicates.append(movie)
    return duplicates


def create_file():
    import random
    movies_list = ['Aba', 'Thor', 'X-men']
    with open('movies.txt', 'w') as f:
        for x in range(5000000):
            f.write(random.choice(movies_list) + "\n")
        f.write("Eyal \n")


if __name__ == '__main__':
    # create_file()
    find_duplicate_movies()
