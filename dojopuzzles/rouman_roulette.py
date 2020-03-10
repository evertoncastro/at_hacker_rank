from unittest import TestCase


def rouman_roulette(total_people, jump):
    people = list(range(1, total_people+1))
    to_kill = 0
    while len(people) > 1:
        to_kill += (jump-1)
        print(people.pop(to_kill))
        to_kill += 1
    



class TestRoumanRoulette(TestCase):

    def test_rouman_roulette(self):
        result = rouman_roulette(5, 2)
        self.assertEqual(result, 4)






