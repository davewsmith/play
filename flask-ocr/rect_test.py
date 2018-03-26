import unittest
from rect import Rect


class RectTest(unittest.TestCase):

    def test_area_of_degenerate_rect(self):
        r = Rect(0,0, 0,0)
        self.assertEqual(0, r.area)

    def test_area_of_non_simple_rect(self):
        r = Rect(10,10, 20,20)
        self.assertEqual(100, r.area)

    def test_height_and_width(self):
        r = Rect(10,10, 47,83)
        self.assertEqual(37, r.width)
        self.assertEqual(73, r.height)

    def test_intersect_of_non_overlapping_rects(self):
        r1 = Rect(10,20, 20,30)
        r2 = Rect(10,30, 20,40)  # abuts the bottom of r1 without intersecting
        r3 = Rect(20,20, 30,40)  # abuts the right of r1 without intersecting
        self.assertIsNone(r1.intersect(r2))
        self.assertIsNone(r2.intersect(r1))
        self.assertIsNone(r1.intersect(r3))
        self.assertIsNone(r3.intersect(r1))

    def test_intersect_of_rect_with_itself(self):
        r1 = Rect(10,20, 20,30)
        self.assertEqual(r1, r1, msg="Sanity check")
        self.assertEqual(r1, r1.intersect(r1))

    def test_intersect_by_full_containment(self):
        r1 = Rect(10,10, 25,25)
        r2 = Rect(15,15, 20,20)  # fully contained within r1
        self.assertEqual(r2, r1.intersect(r2))
        self.assertEqual(r2, r2.intersect(r1))

    def test_intersect_by_partial_intersection(self):
        r1 = Rect(10,10, 30,30)
        r2 = Rect(20,20, 40,40)
        intersection = Rect(20,20, 30,30)
        self.assertEqual(intersection, r1.intersect(r2))
        self.assertEqual(intersection, r2.intersect(r1))

    def test_intersect_by_crossing(self):
        r1 = Rect(20,0, 20,30)
        r2 = Rect(10,10, 30,20)
        intersection = Rect(20,10, 20,20)
        self.assertEqual(intersection, r1.intersect(r2))
        self.assertEqual(intersection, r2.intersect(r1))
