import contextlib

my_cars = ['Dacia', 'Audi', 'Mercedes-Benz', 'Jaguar', 'Renault']
age_by_person = {'Alex': '28', 'Marius': '22', 'Vlad': '45', 'Gabi': '23', 'Andrei': '25'}


@contextlib.contextmanager
def just_some_exceptions():

    try:
        yield 'Well done!'
    except KeyError:
        raise KeyError
    except IndexError:
        raise IndexError
    except StopIteration:
        raise RuntimeError("generator didn't yield") from None


with just_some_exceptions() as exception:
    # test1 = my_cars[2]
    # test2 = my_cars[6]
    # test3 = age_by_person['Marius']
    test4 = age_by_person['Adrian']
    # print(test1)
    # print(test2)
    # print(test3)
    print(test4)

print('Task done!')
