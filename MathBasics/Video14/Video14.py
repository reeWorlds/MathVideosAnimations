import math
from manim import *

def get_angle(a, b, c):
	ba = a.get_center() - b.get_center()
	bc = c.get_center() - b.get_center()
	cosine_angle = (ba[0]*bc[0] + ba[1]*bc[1]) / (math.sqrt(ba[0]**2 + ba[1]**2) * math.sqrt(bc[0]**2 + bc[1]**2))
	angle = math.acos(cosine_angle)

	return math.degrees(angle)

def getAngleSumStr(pa, pb, pc, pd):
	angle_BAD = get_angle(pb, pa, pd)
	angle_BCD = get_angle(pb, pc, pd)
	sum_angle = angle_BAD + angle_BCD

	return "{:.1f}".format(sum_angle)

def getColor(pa, pb, pc, pd):
	angle_BAD = get_angle(pb, pa, pd)
	angle_BCD = get_angle(pb, pc, pd)
	sum_angle = angle_BAD + angle_BCD

	if sum_angle <= 179.8:
		return RED
	elif sum_angle >= 180.2:
		return YELLOW
	else:
		return BLACK

def find_intersection_circle(c, p1, p2):
	# Calculate slopes of lines from center to points
	m1 = (c[1] - p1.get_center()[1]) / (c[0] - p1.get_center()[0])
	m2 = (c[1] - p2.get_center()[1]) / (c[0] - p2.get_center()[0])

	# Calculate slopes of tangent lines
	if m1 != 0:
		m1_tangent = -1 / m1
	else:
		m1_tangent = np.inf

	if m2 != 0:
		m2_tangent = -1 / m2
	else:
		m2_tangent = np.inf

	# Calculate y-intercepts of tangent lines
	b1 = p1.get_center()[1] - m1_tangent * p1.get_center()[0]
	b2 = p2.get_center()[1] - m2_tangent * p2.get_center()[0]

	# Calculate intersection point
	if m1_tangent == np.inf or m2_tangent == np.inf:
		print("Tangents are parallel or undefined.")
		return None
	else:
		x_intersection = (b2 - b1) / (m1_tangent - m2_tangent)
		y_intersection = m1_tangent * x_intersection + b1
		intersection_point = np.array([x_intersection, y_intersection, 0])

	return intersection_point

def add_hash_mark(line, offset, n_hashes):
	angle = line.get_angle() + PI * 0.35
	hash_marks = VGroup()
	
	for i in range(n_hashes):
		pos = line.point_from_proportion(0.43 + (i + 1) / (n_hashes + 1) * 0.14)
		mark = Line(pos - offset * rotate_vector(RIGHT, angle), pos + offset * rotate_vector(RIGHT, angle),
					color=line.get_color(), stroke_width = 2)
		hash_marks.add(mark)
	
	return hash_marks

class Quadrilateral(Scene):
	def clearEverything(self):
		self.play(*[FadeOut(mob) for mob in self.mobjects])

	def showa1(self):
		circle = Circle(radius = 3, color = BLACK).shift(3.5 * LEFT)

		points = [Dot(circle.point_from_proportion(d), radius = 0.06, color = BLACK) for d in [0.1, 0.3, 0.65, 0.95]]
		points_g = VGroup(*points)

		sides = [Line(points[i].get_center(), points[(i+1) % 4].get_center(), color = BLACK) for i in range(4)]
		sides_g = VGroup(*sides)

		points_t = [MathTex(letr, font_size = 50, color = BLACK)\
			.shift(points[i].get_center() + 0.12 * (points[i].get_center() - circle.get_center()))\
			  for i, letr in enumerate(["A", "B", "C", "D"])]
		points_t_g = VGroup(*points_t)

		txt1 = MathTex(r"\angle{BAD} = \frown\!BD = \frown\!BCD", color = BLACK, font_size = 40)\
			.shift(2 * UP + 3.3 * RIGHT)
		txt2 = MathTex(r"\angle{BCD} = \frown\!BD = \frown\!BAD", color = BLACK, font_size = 40)\
			.next_to(txt1, DOWN)
		txt3 = MathTex(r"\angle{BAD} + \angle{BCD} = \frown\!BCD + \frown\!BAD = 180^\circ", color = BLACK,
				font_size = 35).next_to(txt2, DOWN)
		
		txt4 = MathTex(r"\angle{A} + \angle{C} = \angle{B} + \angle{D} = 180^\circ", color = BLACK, font_size = 40)\
			.next_to(txt3, DOWN).shift(0.75 * DOWN)
		sur_box_p = SurroundingRectangle(txt4).set_color(color_gradient([BLUE, YELLOW], 100)).set_stroke(width = 5)

		self.wait(2)
		self.play(Create(circle), run_time = 2)
		self.wait(2)
		self.play(Create(points_g, lag_ratio = 0), Write(points_t_g, lag_ratio = 0), run_time = 2)
		self.play(Create(sides_g, lag_ratio = 0), run_time = 2)

		self.wait(2)
		self.play(Write(txt1), run_time = 2)
		self.play(Write(txt2), run_time = 2)
		self.wait(2)
		self.play(Write(txt3), run_time = 2)
		self.wait(2)
		self.play(Write(txt4), run_time = 2)
		self.play(Create(sur_box_p), run_time = 2)

		self.wait(3)

	def showa2(self):
		ay = ValueTracker(2.5)

		circle = always_redraw(lambda: Circle(radius = 2.5, color = BLACK).shift(2.5 * LEFT))

		pa = always_redraw(lambda: Dot(2.5 * LEFT + ay.get_value() * UP, radius = 0.06, color = BLACK))
		pb = always_redraw(lambda: Dot(circle.point_from_proportion(0.55), radius = 0.06, color = BLACK))
		pc = always_redraw(lambda: Dot(circle.point_from_proportion(0.7), radius = 0.06, color = BLACK))
		pd = always_redraw(lambda: Dot(circle.point_from_proportion(0.95), radius = 0.06, color = BLACK))
		points_g = VGroup(pa, pb, pc, pd)

		l1 = always_redraw(lambda: Line(pa.get_center(), pb.get_center(), color = BLACK))
		l2 = always_redraw(lambda: Line(pb.get_center(), pc.get_center(), color = BLACK))
		l3 = always_redraw(lambda: Line(pc.get_center(), pd.get_center(), color = BLACK))
		l4 = always_redraw(lambda: Line(pd.get_center(), pa.get_center(), color = BLACK))
		lines_g = VGroup(l1, l2, l3, l4)

		pa_t = always_redraw(lambda: MathTex("A", font_size = 50, color = BLACK)\
			.shift(pa.get_center() + 0.12 * (pa.get_center() - circle.get_center())))
		pb_t = always_redraw(lambda: MathTex("B", font_size = 50, color = BLACK)\
			.shift(pb.get_center() + 0.12 * (pb.get_center() - circle.get_center())))
		pc_t = always_redraw(lambda: MathTex("C", font_size = 50, color = BLACK)\
			.shift(pc.get_center() + 0.12 * (pc.get_center() - circle.get_center())))
		pd_t = always_redraw(lambda: MathTex("D", font_size = 50, color = BLACK)\
			.shift(pd.get_center() + 0.12 * (pd.get_center() - circle.get_center())))
		points_t_g = VGroup(pa_t, pb_t, pc_t, pd_t)

		txt1 = always_redraw(lambda:MathTex(r"\angle{BAD} + \angle{BCD} = " + getAngleSumStr(pa, pb, pc, pd)\
		   + r"^\circ", color = getColor(pa, pb, pc, pd), font_size = 40).shift(1 * UP + 3.5 * RIGHT))

		self.wait(2)
		self.play(Create(circle), run_time = 2)
		self.play(Create(points_g, lag_ratio = 0), Create(lines_g, lag_ratio = 0), Write(points_t_g, lag_ratio = 0),
		   run_time = 2)

		self.wait(2)
		self.play(Write(txt1), run_time = 2)

		self.wait(2)
		self.play(ay.animate.set_value(1.5), run_time = 2)
		self.wait(2)
		self.play(ay.animate.set_value(3.3), run_time = 2)
		self.wait(2)
		self.play(ay.animate.set_value(2.5), run_time = 2)

		self.wait(3)

	def showa3(self):
		po = Dot(ORIGIN, color = BLACK, radius = 0.05).shift(2 * LEFT)
		circ = Circle(radius = 2, color = BLACK, stroke_width = 2).move_to(po.get_center())

		pf = Dot(circ.point_from_proportion(0.01), radius = 0.05, color = BLACK)
		pg = Dot(circ.point_from_proportion(0.34), radius = 0.05, color = BLACK)
		ph = Dot(circ.point_from_proportion(0.61), radius = 0.05, color = BLACK)
		pj = Dot(circ.point_from_proportion(0.78), radius = 0.05, color = BLACK)
		points_tangent_g = VGroup(pf, pg, ph, pj)

		pf_t = MathTex("F", font_size = 40, color = BLACK).next_to(pf, RIGHT).shift(0.2 * LEFT)
		pg_t = MathTex("G", font_size = 40, color = BLACK).next_to(pg, UP).shift(0.2 * DOWN)
		ph_t = MathTex("H", font_size = 40, color = BLACK).next_to(ph, LEFT).shift(0.2 * RIGHT + 0.1 * DOWN)
		pj_t = MathTex("J", font_size = 40, color = BLACK).next_to(pj, DOWN).shift(0.2 * UP)
		points_tangent_g_t = VGroup(pf_t, pg_t, ph_t, pj_t)

		pa = Dot(find_intersection_circle(circ.get_center(), pf, pg), radius = 0.05, color = BLACK)
		pb = Dot(find_intersection_circle(circ.get_center(), pg, ph), radius = 0.05, color = BLACK)
		pc = Dot(find_intersection_circle(circ.get_center(), ph, pj), radius = 0.05, color = BLACK)
		pd = Dot(find_intersection_circle(circ.get_center(), pj, pf), radius = 0.05, color = BLACK)
		points_g = VGroup(pa, pb, pc, pd)

		pa_t = MathTex("A", font_size = 40, color = BLACK).next_to(pa, RIGHT).shift(0.2 * LEFT)
		pb_t = MathTex("B", font_size = 40, color = BLACK).next_to(pb, LEFT).shift(0.2 * RIGHT)
		pc_t = MathTex("C", font_size = 40, color = BLACK).next_to(pc, DOWN).shift(0.2 * UP)
		pd_t = MathTex("D", font_size = 40, color = BLACK).next_to(pd, DOWN).shift(0.2 * UP)
		points_g_t = VGroup(pa_t, pb_t, pc_t, pd_t)

		l1 = Line(pa.get_center(), pb.get_center(), color = BLACK, stroke_width = 2)
		l2 = Line(pb.get_center(), pc.get_center(), color = BLACK, stroke_width = 2)
		l3 = Line(pc.get_center(), pd.get_center(), color = BLACK, stroke_width = 2)
		l4 = Line(pd.get_center(), pa.get_center(), color = BLACK, stroke_width = 2)
		lines_g = VGroup(l1, l2, l3, l4)

		marks1_1 = add_hash_mark(Line(pa.get_center(), pf.get_center(), color = BLACK), 0.1, 1)
		marks1_2 = add_hash_mark(Line(pa.get_center(), pg.get_center(), color = BLACK), 0.1, 1)
		txt1 = MathTex("AF = AG = x", font_size = 40, color = BLACK).shift(3.5 * RIGHT + 3 * UP)

		marks2_1 = add_hash_mark(Line(pb.get_center(), pg.get_center(), color = BLACK), 0.1, 2)
		marks2_2 = add_hash_mark(Line(pb.get_center(), ph.get_center(), color = BLACK), 0.1, 2)
		txt2 = MathTex("BG = BH = y", font_size = 40, color = BLACK).next_to(txt1, DOWN)

		marks3_1 = add_hash_mark(Line(pc.get_center(), ph.get_center(), color = BLACK), 0.1, 3)
		marks3_2 = add_hash_mark(Line(pc.get_center(), pj.get_center(), color = BLACK), 0.1, 3)
		txt3 = MathTex("CH = CJ = u", font_size = 40, color = BLACK).next_to(txt2, DOWN)

		marks4_1 = add_hash_mark(Line(pd.get_center(), pj.get_center(), color = BLACK), 0.1, 4)
		marks4_2 = add_hash_mark(Line(pd.get_center(), pf.get_center(), color = BLACK), 0.1, 4)
		txt4 = MathTex("DJ = DF = v", font_size = 40, color = BLACK).next_to(txt3, DOWN)

		txt5 = MathTex("AD + CB = AB + CD", font_size = 40, color = BLACK).next_to(txt4, DOWN).shift(0.5 * DOWN)
		sur_box_p = SurroundingRectangle(txt5).set_color(color_gradient([BLUE, YELLOW], 100)).set_stroke(width = 5)

		txt6 = MathTex("x + v + y + u = x + y + u + v", font_size = 40, color = BLACK).next_to(txt5, DOWN)\
			.shift(0.2 * DOWN)

		self.wait(2)
		self.play(Create(po), Create(circ), run_time = 2)
		self.wait(2)
		self.play(Create(points_g, lag_ratio = 0), Write(points_g_t, lag_ratio = 0), run_time = 2)
		self.play(Create(lines_g, lag_ratio = 0), run_time = 2)
		self.wait(2)
		self.play(Create(points_tangent_g, lag_ratio = 0), Write(points_tangent_g_t, lag_ratio = 0), run_time = 2)

		self.wait(2)
		self.play(Write(txt1), Create(marks1_1, lag_ratio = 0), Create(marks1_2, lag_ratio = 0), run_time = 2)
		self.play(Write(txt2), Create(marks2_1, lag_ratio = 0), Create(marks2_2, lag_ratio = 0), run_time = 2)
		self.play(Write(txt3), Create(marks3_1, lag_ratio = 0), Create(marks3_2, lag_ratio = 0), run_time = 2)
		self.play(Write(txt4), Create(marks4_1, lag_ratio = 0), Create(marks4_2, lag_ratio = 0), run_time = 2)

		self.wait(2)
		self.play(Write(txt5), run_time = 2)
		self.wait(2)
		self.play(Write(txt6), run_time = 2)

		self.wait(2)
		self.play(Create(sur_box_p), run_time = 2)

		self.wait(2)

	def showa4(self):
		circ = Circle(radius = 2, color = BLACK, stroke_width = 2).move_to(2 * LEFT)

		pf = Dot(circ.point_from_proportion(0.21), radius = 0.05, color = BLACK)
		pg = Dot(circ.point_from_proportion(0.54), radius = 0.05, color = BLACK)
		ph = Dot(circ.point_from_proportion(0.81), radius = 0.05, color = BLACK)
		pj = Dot(circ.point_from_proportion(0.98), radius = 0.05, color = BLACK)

		pa = Dot(find_intersection_circle(circ.get_center(), pf, pg), radius = 0.05, color = BLACK)
		pb = Dot(find_intersection_circle(circ.get_center(), pg, ph), radius = 0.05, color = BLACK)
		pc = Dot(find_intersection_circle(circ.get_center(), ph, pj), radius = 0.05, color = BLACK)
		pe = Dot(find_intersection_circle(circ.get_center(), pj, pf), radius = 0.05, color = BLACK)
		pd = Dot(pe.get_center() + (pe.get_center() - pc.get_center()) * 0.5, radius = 0.05, color = BLACK)
		points_g = VGroup(pa, pb, pc, pd)

		pa_t = MathTex("A", font_size = 40, color = BLACK).next_to(pa, LEFT).shift(0.2 * RIGHT)
		pb_t = MathTex("B", font_size = 40, color = BLACK).next_to(pb, LEFT).shift(0.2 * RIGHT)
		pc_t = MathTex("C", font_size = 40, color = BLACK).next_to(pc, DOWN).shift(0.2 * UP)
		pe_t = MathTex("E", font_size = 40, color = BLACK).next_to(pe, RIGHT).shift(0.2 * LEFT)
		pd_t = MathTex("D", font_size = 40, color = BLACK).next_to(pd, UP).shift(0.2 * DOWN)
		points_g_t = VGroup(pa_t, pb_t, pc_t, pd_t)

		l1 = Line(pa.get_center(), pb.get_center(), color = BLACK, stroke_width = 2)
		l2 = Line(pb.get_center(), pc.get_center(), color = BLACK, stroke_width = 2)
		l3 = Line(pc.get_center(), pd.get_center(), color = BLACK, stroke_width = 2)
		l4 = Line(pd.get_center(), pa.get_center(), color = BLACK, stroke_width = 2)
		l5 = Line(pa.get_center(), pe.get_center(), color = BLACK, stroke_width = 2)
		lines_g = VGroup(l1, l2, l3, l4)

		txt1 = MathTex("AB + CE = AE + BC", font_size = 40, color = BLACK).shift(3.5 * RIGHT + 2.5 * UP)
		
		txt2 = MathTex("AB + CD = BC + AD", font_size = 40, color = BLACK).next_to(txt1, DOWN).shift(0.3 * DOWN)
		txt3 = MathTex("AB + CE + ED = BC + AD", font_size = 40, color = BLACK).next_to(txt2, DOWN)
		txt4 = MathTex("AB + CE = BC + AD - ED", font_size = 40, color = BLACK).next_to(txt3, DOWN)
		
		txt5 = MathTex("BC + AD - ED = AE + BC", font_size = 40, color = BLACK).next_to(txt4, DOWN).shift(0.4 * DOWN)
		txt6 = MathTex("AE + ED = AD", font_size = 40, color = BLACK).next_to(txt5, DOWN)

		txt6_cross = Cross(txt6, stroke_width = 6, color = RED)

		self.wait(2)
		self.play(Create(circ), run_time = 2)
		self.wait(2)
		self.play(Create(points_g, lag_ratio = 0), Write(points_g_t, lag_ratio = 0), run_time = 2)
		self.play(Create(lines_g, lag_ratio = 0), run_time = 2)

		self.wait(2)
		self.play(Create(pe), Write(pe_t), Create(l5), run_time = 2)

		self.wait(2)
		self.play(Write(txt1), run_time = 2)
		self.wait(2)
		self.play(Write(txt2), run_time = 2)
		self.wait(2)
		self.play(Write(txt3), run_time = 2)
		self.wait(2)
		self.play(Write(txt4), run_time = 2)
		self.wait(2)
		self.play(Write(txt5), run_time = 2)
		self.wait(2)
		self.play(Write(txt6), run_time = 2)
		self.wait(2)
		self.play(Create(txt6_cross), run_time = 2)

		self.wait(2)

	def construct(self):
		self.camera.background_color = WHITE

		self.showa1()
		self.clearEverything()
		self.showa2()
		self.clearEverything()
		self.showa3()
		self.clearEverything()
		self.showa4()
		self.clearEverything()