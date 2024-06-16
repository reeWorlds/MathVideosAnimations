from manim import *
import numpy as np

def find_circumcenter(A, B, C):
	D = (A + B) / 2
	E = (B + C) / 2
	
	m_AB = (B[1] - A[1]) / (B[0] - A[0]) if B[0] != A[0] else None
	m_BC = (C[1] - B[1]) / (C[0] - B[0]) if C[0] != B[0] else None
	
	m_D = -1/m_AB if m_AB is not None else 0
	m_E = -1/m_BC if m_BC is not None else 0
	
	x = (m_D * D[0] - m_E * E[0] + E[1] - D[1]) / (m_D - m_E)
	if m_AB is not None:
		y = m_D * (x - D[0]) + D[1]
	else:
		y = m_E * (x - E[0]) + E[1]
	
	circumcenter = np.array([x, y, 0])
	
	return circumcenter.tolist()

def add_hash_mark(line, offset):
	angle = line.get_angle() + PI * 0.35
	pos = line.point_from_proportion(0.5)
	
	mark = Line(pos - offset * rotate_vector(RIGHT, angle), pos + offset * rotate_vector(RIGHT, angle),
			color=line.get_color(), stroke_width = 2)

	return mark

class SinTheorem(Scene):
	def clearEverything(self):
		self.play(*[FadeOut(mob) for mob in self.mobjects])

	def showa1(self):
		myTemplate = TexTemplate()
		myTemplate.add_to_preamble(r"\usepackage{xcolor}")

		coordsA = [0, 0.25, 0]
		coordsB = [-1, 2.25, 0]
		coordsC = [-6.25, 1.25, 0]

		pa = Dot(coordsA, radius = 0.05, color = BLACK)
		pb = Dot(coordsB, radius = 0.05, color = BLACK)
		pc = Dot(coordsC, radius = 0.05, color = BLACK)
		points = VGroup(pa, pb, pc)

		pa_t = MathTex("A", color = BLACK, font_size = 50).next_to(pa, DOWN).shift(UP * 0.5 + RIGHT * 0.3)
		pb_t = MathTex("B", color = BLACK, font_size = 50).next_to(pb, UP).shift(DOWN * 0.1 + RIGHT * 0.1)
		pc_t = MathTex("C", color = BLACK, font_size = 50).next_to(pc, LEFT).shift(RIGHT * 0.1)
		points_t = VGroup(pa_t, pb_t, pc_t)

		la = Line(pb.get_center(), pc.get_center(), color = GREEN, stroke_width = 4)
		lb = Line(pc.get_center(), pa.get_center(), color = BLUE, stroke_width = 4)
		lc = Line(pa.get_center(), pb.get_center(), color = RED, stroke_width = 4)
		lines = VGroup(la, lb, lc)

		la_t = MathTex("a", color = GREEN, font_size = 50).next_to(la, UP).shift(DOWN * 0.6)
		lb_t = MathTex("b", color = BLUE, font_size = 50).next_to(lb, UP).shift(DOWN * 0.6)
		lc_t = MathTex("c", color = RED, font_size = 50).next_to(lc, LEFT).shift(RIGHT * 0.6)
		lines_t = VGroup(la_t, lb_t, lc_t)

		ang_a = Angle(Line(pa, pb), Line(pa, pc), radius = 0.5, color = BLACK)
		ang_b = Angle(Line(pb, pc), Line(pb, pa), radius = 0.5, color = BLACK)
		ang_c = Angle(Line(pc, pa), Line(pc, pb), radius = 0.8, color = BLACK)
		angles = VGroup(ang_a, ang_b, ang_c)

		ang_a_t = MathTex(r"\alpha", color = BLACK, font_size = 40).next_to(ang_a, LEFT)\
			.shift(UP * 0.2 + RIGHT * 0.25)
		ang_b_t = MathTex(r"\beta", color = BLACK, font_size = 40).next_to(ang_b, DOWN)\
			.shift(UP * 0.2 + LEFT * 0.2)
		ang_c_t = MathTex(r"\gamma", color = BLACK, font_size = 40).next_to(ang_c, RIGHT).shift(LEFT * 0.1)
		angles_t = VGroup(ang_a_t, ang_b_t, ang_c_t)

		center_coords = find_circumcenter(np.array(coordsA), np.array(coordsB), np.array(coordsC))
		center_o = Dot(center_coords, radius = 0.05, color = BLACK)
		center_o_t = MathTex("O", color = BLACK, font_size = 50).next_to(center_o, DOWN)\
			.shift(UP * 0.15 + RIGHT * 0.1)
		
		R_val = np.linalg.norm(np.array(coordsA) - np.array(center_coords))
		circle = Circle(radius = R_val, color = BLACK).move_to(center_coords)

		radius = Line(center_o.get_center(), circle.point_from_proportion(0.65), color = BLACK,
			   stroke_width = 4)
		radius_t = MathTex("R", color = BLACK, font_size = 50).next_to(radius, LEFT).shift(RIGHT * 0.9)

		formula1 = MathTex(r"\dfrac{\textcolor{green}{a}}{\sin(\alpha)} = \dfrac{\textcolor{blue}{b}}"
					r"{\sin(\beta)} = \dfrac{\textcolor{red}{c}}{\sin(\gamma)}", tex_template = myTemplate,
					color = BLACK, font_size = 50).shift(RIGHT * 2.75 + UP * 2)

		formula2 = MathTex(r" = 2R", color = BLACK, font_size = 45).next_to(formula1, RIGHT)

		self.wait(2)
		self.play(Create(points, lag_ratio = 0), Write(points_t, lag_ratio = 0), run_time = 2)
		self.play(Create(lines, lag_ratio = 0), Write(lines_t, lag_ratio = 0), run_time = 2)
		self.play(Create(angles, lag_ratio = 0), Write(angles_t, lag_ratio = 0), run_time = 2)
		
		self.wait(2)
		self.play(Write(formula1), run_time = 2)

		self.wait(2)
		self.play(Create(center_o), Write(center_o_t), run_time = 2)
		self.play(Create(circle), run_time = 2)
		self.play(Create(radius), Write(radius_t), run_time = 2)
		
		self.wait(2)
		self.play(Write(formula2), run_time = 2)
		
		self.wait(2)

	def showa2(self):
		coordsA = [0.5, -2, 0]
		coordsB = [-0.5, 2.25, 0]
		coordsC = [-5.5, 1.25, 0]

		pa = Dot(coordsA, radius = 0.05, color = BLACK)
		pb = Dot(coordsB, radius = 0.05, color = BLACK)
		pc = Dot(coordsC, radius = 0.05, color = BLACK)
		points = VGroup(pa, pb, pc)

		pa_t = MathTex("A", color = BLACK, font_size = 50).next_to(pa, DOWN).shift(UP * 0.5 + RIGHT * 0.3)
		pb_t = MathTex("B", color = BLACK, font_size = 50).next_to(pb, UP).shift(DOWN * 0.1 + RIGHT * 0.1)
		pc_t = MathTex("C", color = BLACK, font_size = 50).next_to(pc, LEFT).shift(RIGHT * 0.1)
		points_t = VGroup(pa_t, pb_t, pc_t)

		la = Line(pb.get_center(), pc.get_center(), color = GREEN, stroke_width = 4)
		lb = Line(pc.get_center(), pa.get_center(), color = BLUE, stroke_width = 4)
		lc = Line(pa.get_center(), pb.get_center(), color = RED, stroke_width = 4)
		lines = VGroup(la, lb, lc)

		ang_a = Angle(Line(pa, pb), Line(pa, pc), radius = 0.5, color = BLACK)
		ang_a_t = MathTex(r"\alpha", color = BLACK, font_size = 50).next_to(ang_a, LEFT)\
			.shift(UP * 0.25 + RIGHT * 0.35)
		form1 = MathTex(r"\alpha = 45^\circ", color = BLACK, font_size = 60).shift(UP * 3 + RIGHT * 2.5)

		ang_b = Angle(Line(pb, pc), Line(pb, pa), radius = 0.5, color = BLACK)
		ang_b_t = MathTex(r"\beta", color = BLACK, font_size = 50).next_to(ang_b, DOWN)\
			.shift(UP * 0.2 + LEFT * 0.2)
		form2 = MathTex(r"\beta = 60^\circ", color = BLACK, font_size = 60).next_to(form1, RIGHT)\
			.shift(RIGHT * 0.5)

		la_t = MathTex("6", color = GREEN, font_size = 50).next_to(la, UP).shift(DOWN * 0.6)
		form3 = MathTex(r"CB = 6", color = BLACK, font_size = 60).next_to(form1, DOWN)

		lb_t = MathTex("x", color = BLUE, font_size = 50).next_to(lb, DOWN).shift(UP * 1.5)
		form4 = MathTex(r"x - ?", color = BLACK, font_size = 60).next_to(form2, DOWN)
		
		
		formula1 = MathTex(r"\frac{CB}{\sin(\alpha)} = \frac{AC}{\sin(\beta)}", color = BLACK,
					font_size = 40).shift(UP * 0.75 + RIGHT * 3.8)
		formula2 = MathTex(r"\frac{6}{\sin(45^\circ)} = \frac{x}{\sin(60^\circ)}", color = BLACK,
					font_size = 40).next_to(formula1, DOWN)
		formula3 = MathTex(r"\frac{6}{\tfrac{\sqrt{2}}{2}} = \frac{x}{\tfrac{\sqrt{3}}{2}}", color = BLACK,
					font_size = 40).next_to(formula2, DOWN)
		formula4 = MathTex(r"\frac{6}{\sqrt{2}} = \frac{x}{\sqrt{3}}", color = BLACK,
					font_size = 40).next_to(formula2, DOWN)
		formula5 = MathTex(r"3\sqrt{2} = \frac{x}{\sqrt{3}}", color = BLACK,
					font_size = 40).next_to(formula2, DOWN)

		self.wait(2)
		self.play(Create(points, lag_ratio = 0), Write(points_t, lag_ratio = 0), run_time = 2)
		self.play(Create(lines, lag_ratio = 0), run_time = 2)

		self.wait(2)
		self.play(Create(ang_a), Write(ang_a_t), Write(form1), run_time = 2)
		self.wait(2)
		self.play(Create(ang_b), Write(ang_b_t), Write(form2), run_time = 2)
		self.wait(2)
		self.play(Write(la_t), Write(form3), run_time = 2)
		self.wait(2)
		self.play(Write(lb_t), Write(form4), run_time = 2)

		self.wait(2)
		self.play(Write(formula1), run_time = 2)
		self.wait(2)
		self.play(Write(formula2), run_time = 2)
		self.wait(2)
		self.play(Write(formula3), run_time = 2)
		self.wait(2)
		self.play(Transform(formula3, formula4), run_time = 2)
		self.wait(2)
		self.play(Transform(formula3, formula5), run_time = 2)

		formula6 = MathTex(r"AC = x = 3\sqrt{6}", color = BLACK,
					font_size = 40).next_to(formula3, DOWN)

		self.wait(2)
		self.play(Write(formula6), run_time = 2)

		self.wait(3)

	def showa3(self):
		myTemplate = TexTemplate()
		myTemplate.add_to_preamble(r"\usepackage{xcolor}")

		coordsA = [0, 0.25, 0]
		coordsB = [-5.95, 1.4, 0]
		coordsC = [-1, 2.25, 0]

		pa = Dot(coordsA, radius = 0.05, color = BLACK)
		pb = Dot(coordsB, radius = 0.05, color = BLACK)
		pc = Dot(coordsC, radius = 0.05, color = BLACK)
		points = VGroup(pa, pb, pc)

		pa_t = MathTex("A", color = BLACK, font_size = 50).next_to(pa, DOWN).shift(UP * 0.5 + RIGHT * 0.3)
		pb_t = MathTex("B", color = BLACK, font_size = 50).next_to(pb, LEFT).shift(RIGHT * 0.1)
		pc_t = MathTex("C", color = BLACK, font_size = 50).next_to(pc, UP).shift(DOWN * 0.1 + RIGHT * 0.1)
		points_t = VGroup(pa_t, pb_t, pc_t)

		la = Line(pb.get_center(), pc.get_center(), color = GREEN, stroke_width = 4)
		lb = Line(pc.get_center(), pa.get_center(), color = BLUE, stroke_width = 4)
		lc = Line(pa.get_center(), pb.get_center(), color = RED, stroke_width = 4)
		lines = VGroup(la, lb, lc)

		la_t = MathTex("a", color = GREEN, font_size = 50).next_to(la, UP).shift(DOWN * 0.6)
		
		ang_a = Angle(Line(pa, pc), Line(pa, pb), radius = 0.5, color = BLACK)
		ang_a_t = MathTex(r"\alpha", color = BLACK, font_size = 35).next_to(ang_a, LEFT)\
			.shift(UP * 0.25 + RIGHT * 0.4)

		center_coords = find_circumcenter(np.array(coordsA), np.array(coordsB), np.array(coordsC))
		center_o = Dot(center_coords, radius = 0.05, color = BLACK)
		center_o_t = MathTex("O", color = BLACK, font_size = 50).next_to(center_o, DOWN)\
			.shift(UP * 0.2 + LEFT * 0.2)
		
		radius = np.linalg.norm(np.array(coordsA) - np.array(center_coords))
		circle = Circle(radius = radius, color = BLACK).move_to(center_coords)

		rad1_l = Line(center_o.get_center(), pb.get_center(), color = BLACK, stroke_width = 4)
		rad1_l_t = MathTex("R", color = BLACK, font_size = 40).next_to(rad1_l, DOWN).shift(UP * 0.8)

		self.wait(2)
		self.play(Create(points, lag_ratio = 0), Write(points_t, lag_ratio = 0), run_time = 2)
		self.play(Create(lines, lag_ratio = 0), Write(la_t), run_time = 2)
		self.play(Create(ang_a), Write(ang_a_t), run_time = 2)

		self.wait(2)
		self.play(Create(center_o), Write(center_o_t), Create(circle), run_time = 2)
		self.play(Create(rad1_l), Write(rad1_l_t), run_time = 2)

		pd = Dot(2 * center_o.get_center() - pb.get_center(), radius = 0.05, color = BLACK)
		pd_t = MathTex("D", color = BLACK, font_size = 50).next_to(pd, DOWN).shift(UP * 0.5 + RIGHT * 0.3)
		rad2_l = Line(center_o.get_center(), pd.get_center(), color = BLACK, stroke_width = 4)
		rad2_l_t = MathTex("R", color = BLACK, font_size = 40).next_to(rad2_l, DOWN).shift(UP * 0.8)

		self.wait(2)
		self.play(Create(pd), Write(pd_t), Create(rad2_l), Write(rad2_l_t), run_time = 2)
		
		ldc = Line(pd.get_center(), pc.get_center(), color = BLACK, stroke_width = 4)
		ang_bdc = Angle(Line(pd, pc), Line(pd, pb), radius = 0.5, color = BLACK)
		ang_bdc_t = MathTex(r"\alpha", color = BLACK, font_size = 35).next_to(ang_bdc, LEFT)\
			.shift(UP * 0.25 + RIGHT * 0.4)

		self.wait(2)
		self.play(Create(ldc), Create(ang_bdc), Write(ang_bdc_t), run_time = 2)

		rad3_l = Line(center_o.get_center(), pc.get_center(), color = BLACK, stroke_width = 4)
		rad3_l_t = MathTex("R", color = BLACK, font_size = 40).next_to(rad3_l, RIGHT)\
			.shift(LEFT * 1.3 + DOWN * 0.1)

		self.wait(2)
		self.play(Create(rad3_l), Write(rad3_l_t), run_time = 2)

		mark1 = add_hash_mark(rad3_l, 0.15)
		mark2 = add_hash_mark(rad2_l, 0.15)
		ang_ocd = Angle(Line(pc, center_o), Line(pc, pd), radius = 0.35, color = BLACK)
		ang_ocd_t = MathTex(r"\alpha", color = BLACK, font_size = 35).next_to(ang_ocd, DOWN)\
			.shift(UP * 0.15)

		self.wait(2)
		self.play(Create(mark1), Create(mark2), run_time = 2)
		self.play(Create(ang_ocd), Write(ang_ocd_t), run_time = 2)

		ang_obc = Angle(Line(pb, center_o), Line(pb, pc), radius = 0.5, color = BLACK)
		ang_obc_t = MathTex(r"\beta", color = BLACK, font_size = 35).next_to(ang_obc, RIGHT)\
			.shift(LEFT * 0.15)
		mark3 = add_hash_mark(rad1_l, 0.15)
		ang_bco = Angle(Line(pc, pb), Line(pc, center_o), radius = 0.35, color = BLACK)
		ang_bco_t = MathTex(r"\beta", color = BLACK, font_size = 35).next_to(ang_bco, DOWN)\
			.shift(UP * 0.35 + LEFT * 0.2)

		self.wait(2)
		self.play(Create(ang_obc), Write(ang_obc_t), run_time = 2)
		self.play(Create(mark3), run_time = 2)
		self.play(Create(ang_bco), Write(ang_bco_t), run_time = 2)

		txt1 = MathTex(r"\Delta BCD", font_size=50, color = BLACK).shift(RIGHT * 3.5 + UP * 1.5)
		txt2 = MathTex(r"\alpha + \beta + (\alpha + \beta) = 180^\circ", font_size=50, color = BLACK)\
			.next_to(txt1, DOWN)
		txt3 = MathTex(r"2(\alpha + \beta) = 180^\circ", font_size=50, color = BLACK).next_to(txt2, DOWN)
		txt4 = MathTex(r"\alpha + \beta = 90^\circ", font_size=50, color = BLACK).next_to(txt3, DOWN)

		ang_bcd = RightAngle(Line(pc, pb), Line(pc, pd), length = 0.4, color = BLACK)

		self.wait(2)
		self.play(Write(txt1), run_time = 2)
		self.play(Write(txt2), run_time = 2)
		self.play(Write(txt3), run_time = 2)
		self.play(Write(txt4), run_time = 2)
		self.wait(2)
		self.play(Create(ang_bcd), run_time = 2)

		fadeGroup = VGroup(txt1, txt2, txt3, txt4, mark1, mark2, mark3, rad3_l, rad3_l_t, ang_obc, ang_obc_t,
					 ang_ocd, ang_ocd_t, ang_bco, ang_bco_t)

		m_font_size = 45

		txt5 = MathTex(r"\Delta BCD", font_size=50, color = BLACK).shift(RIGHT * 3.5 + UP * 3)
		txt6 = MathTex(r"\sin(\alpha) = \frac{\textcolor{green}{a}}{2R}", font_size=m_font_size, color = BLACK, 
				tex_template = myTemplate).next_to(txt5, DOWN)
		txt7 = MathTex(r"\frac{\textcolor{green}{a}}{\sin(\alpha)} = 2R", font_size=m_font_size, color = BLACK,
				tex_template = myTemplate).next_to(txt5, DOWN)

		txt8 = MathTex(r"\frac{\textcolor{blue}{b}}{\sin(\beta)} = 2R", font_size=m_font_size, color = BLACK,
				tex_template = myTemplate).next_to(txt7, DOWN)
		txt9 = MathTex(r"\frac{\textcolor{red}{c}}{\sin(\gamma)} = 2R", font_size=m_font_size, color = BLACK,
				tex_template = myTemplate).next_to(txt8, DOWN)

		theorem = MathTex(r"\dfrac{\textcolor{green}{a}}{\sin(\alpha)} = \dfrac{\textcolor{blue}{b}}"
					r"{\sin(\beta)} = \dfrac{\textcolor{red}{c}}{\sin(\gamma)} = 2R",
				   tex_template = myTemplate, color = BLACK, font_size = m_font_size).next_to(txt9, DOWN)\
					   .shift(0.6 * DOWN)
		sur_box = SurroundingRectangle(theorem).set_color(color_gradient([BLUE, YELLOW], 100))\
			.set_stroke(width = 5)

		self.wait(2)
		self.play(FadeOut(fadeGroup, lag_ratio = 0), run_time = 2)
		self.wait(2)
		self.play(Write(txt5), run_time = 2)
		self.wait(2)
		self.play(Write(txt6), run_time = 2)
		self.play(Transform(txt6, txt7), run_time = 2)
		self.wait(2)
		self.play(Write(txt8), run_time = 2)
		self.play(Write(txt9), run_time = 2)
		self.wait(2)
		self.play(Write(theorem), run_time = 2)
		self.play(Create(sur_box), run_time = 2)

		self.wait(2)

	def construct(self):
		self.camera.background_color = WHITE

		self.showa1()
		self.clearEverything()
		self.showa2()
		self.clearEverything()
		self.showa3()
		self.clearEverything()
