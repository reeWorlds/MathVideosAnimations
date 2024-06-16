from manim import *
import math


def find_circumcircle(coords):
	x1, y1 = coords[0]
	x2, y2 = coords[1]
	x3, y3 = coords[2]

	D = 2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

	Ux = ((x1**2 + y1**2) * (y2 - y3) + (x2**2 + y2**2) * (y3 - y1) + (x3**2 + y3**2) * (y1 - y2)) / D
	Uy = ((x1**2 + y1**2) * (x3 - x2) + (x2**2 + y2**2) * (x1 - x3) + (x3**2 + y3**2) * (x2 - x1)) / D

	radius = math.sqrt((x1 - Ux)**2 + (y1 - Uy)**2)
	
	return (Ux, Uy), radius

def add_hash_mark(line, offset, n_hashes):
	angle = line.get_angle() + PI * 0.35
	hash_marks = VGroup()
	
	for i in range(n_hashes):
		pos = line.point_from_proportion(0.43 + (i+1)/(n_hashes+1) * 0.14)
		mark = Line(pos - offset * rotate_vector(RIGHT, angle), pos + offset * rotate_vector(RIGHT, angle),
					color=line.get_color(), stroke_width = 2)
		hash_marks.add(mark)
	
	return hash_marks


class CircumscribedCircle(Scene):
	def clearEverything(self):
		self.play(*[FadeOut(mob) for mob in self.mobjects])

	def showa1(self):
		coords = [[-2, -2.5], [-1, 3], [3, 0]]
		
		pa = Dot(coords[0][0] * RIGHT + coords[0][1] * UP, radius = 0.06, color = BLACK)
		pb = Dot(coords[1][0] * RIGHT + coords[1][1] * UP, radius = 0.06, color = BLACK)
		pc = Dot(coords[2][0] * RIGHT + coords[2][1] * UP, radius = 0.06, color = BLACK)
		points = VGroup(pa, pb, pc)

		la = Line(pb.get_center(), pc.get_center(), color = BLACK)
		lb = Line(pa.get_center(), pc.get_center(), color = BLACK)
		lc = Line(pa.get_center(), pb.get_center(), color = BLACK)
		lines = VGroup(la, lb, lc)

		ta = MathTex("A", color = BLACK).next_to(pa, DOWN).shift(0.2 * LEFT + 0.3 * UP)
		tb = MathTex("B", color = BLACK).next_to(pb, UP).shift(0.15 * DOWN)
		tc = MathTex("C", color = BLACK).next_to(pc, RIGHT).shift(0.2 * LEFT)
		labels = VGroup(ta, tb, tc)

		center_c, r_val = find_circumcircle(coords)

		p_center = Dot(center_c[0] * RIGHT + center_c[1] * UP, radius = 0.05, color = BLACK)
		p_center_t = MathTex("O", color = BLACK).next_to(p_center, RIGHT).shift(0.2 * UP)
		circ = Circle(radius = r_val, color = BLACK).move_to(center_c[0] * RIGHT + center_c[1] * UP)

		l_oa = Line(p_center.get_center(), pa.get_center(), color = BLUE)
		l_ob = Line(p_center.get_center(), pb.get_center(), color = BLUE)

		pl = Dot((coords[0][0] + coords[1][0]) / 2 * RIGHT + (coords[0][1] + coords[1][1]) / 2 * UP,
		  radius = 0.06, color = BLACK)
		pl_t = MathTex("L", color = BLACK).next_to(pl, LEFT).shift(0.4 * UP + 0.25 * RIGHT)
		l_ol = Line(p_center.get_center(), pl.get_center(), color = BLACK)

		ang1 = Angle(l_ol, l_oa, radius = 0.4, color = GREEN)
		ang2 = Angle(l_ob, l_ol, radius = 0.4, color = GREEN)

		mark1_1 = add_hash_mark(Line(pl.get_center(), pa.get_center(), color = BLACK), 0.15, 1)
		mark1_2 = add_hash_mark(Line(pl.get_center(), pb.get_center(), color = BLACK), 0.15, 1)

		self.wait(2)
		self.play(Create(points, lag_ratio = 0), run_time = 2)
		self.play(Write(labels, lag_ratio = 0), run_time = 2)
		self.play(Create(lines, lag_ratio = 0), run_time = 2)

		self.wait(2)
		self.play(Create(p_center), Write(p_center_t), run_time = 2)
		self.play(Create(circ), run_time = 2)

		self.wait(2)
		self.play(Create(l_oa), Create(l_ob), run_time = 2)

		self.wait(2)
		self.play(Create(pl), Create(l_ol), Write(pl_t), run_time = 2)
		self.play(Create(ang1), Create(ang2), run_time = 2)

		self.wait(2)
		self.play(Create(mark1_1, lag_ratio = 0), Create(mark1_2, lag_ratio = 0), run_time = 2)

		self.wait(3)

		rang_1 = RightAngle(Line(pl.get_center(), pa.get_center()),
					  Line(pl.get_center(), p_center.get_center()), length = 0.3, color = BLACK)
		big_l = Line(pl.get_center() * 4 - p_center.get_center() * (4 - 1),
			  p_center.get_center() * 4 - pl.get_center() * (4 - 1), color = BLACK)

		pl2 = Dot((coords[0][0] + coords[2][0]) / 2 * RIGHT + (coords[0][1] + coords[2][1]) / 2 * UP,
			radius = 0.06, color = BLACK)
		l_ol2 = Line(p_center.get_center(), pl2.get_center(), color = BLACK)
		rang_2 = RightAngle(Line(pl2.get_center(), pc.get_center()),
					  Line(pl2.get_center(), p_center.get_center()), length = 0.3, color = BLACK)
		pl2_g = VGroup(pl2, l_ol2, rang_2)

		mark2_1 = add_hash_mark(Line(pl2.get_center(), pa.get_center(), color = BLACK), 0.15, 3)
		mark2_2 = add_hash_mark(Line(pl2.get_center(), pc.get_center(), color = BLACK), 0.15, 3)

		pl3 = Dot((coords[1][0] + coords[2][0]) / 2 * RIGHT + (coords[1][1] + coords[2][1]) / 2 * UP,
			radius = 0.06, color = BLACK)
		l_ol3 = Line(p_center.get_center(), pl3.get_center(), color = BLACK)
		rang_3 = RightAngle(Line(pl3.get_center(), pb.get_center()),
					  Line(pl3.get_center(), p_center.get_center()), length = 0.3, color = BLACK)
		pl3_g = VGroup(pl3, l_ol3, rang_3)

		mark3_1 = add_hash_mark(Line(pl3.get_center(), pb.get_center(), color = BLACK), 0.15, 2)
		mark3_2 = add_hash_mark(Line(pl3.get_center(), pc.get_center(), color = BLACK), 0.15, 2)

		self.wait(2)
		self.play(FadeOut(ang1), FadeOut(ang2), FadeOut(l_oa), FadeOut(l_ob), run_time = 2)

		self.wait(2)
		self.play(Create(rang_1), Create(big_l), run_time = 2)

		self.wait(3)
		self.play(FadeOut(big_l), run_time = 2)
		
		self.wait(2)
		self.play(Create(pl2_g, lag_ratio = 0), Create(pl3_g, lag_ratio = 0), Create(mark2_1, lag_ratio = 0),
			Create(mark2_2, lag_ratio = 0), Create(mark3_1, lag_ratio = 0), Create(mark3_2, lag_ratio = 0),
			run_time = 2)

		self.wait(3)

	def construct(self):
		self.camera.background_color = WHITE

		self.showa1()
		self.clearEverything()