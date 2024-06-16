from manim import *

def intersection(line1: Line, line2: Line) -> np.ndarray:
	start1, end1 = line1.get_start_and_end()
	start2, end2 = line2.get_start_and_end()

	direction1 = end1 - start1
	direction2 = end2 - start2

	slope1 = direction1[1] / direction1[0] if direction1[0] != 0 else np.inf
	slope2 = direction2[1] / direction2[0] if direction2[0] != 0 else np.inf

	c1 = start1[1] - slope1 * start1[0]
	c2 = start2[1] - slope2 * start2[0]

	if slope1 == slope2:
		return None
	elif slope1 == np.inf:
		x = start1[0]
		y = slope2 * x + c2
	elif slope2 == np.inf:
		x = start2[0]
		y = slope1 * x + c1
	else:
		x = (c2 - c1) / (slope1 - slope2)
		y = slope1 * x + c1

	return np.array([x, y, 0])

def find_foot_of_perpendicular(line: Line, point: Dot):
	start, end = line.get_start_and_end()
	direction_line = end - start
	slope_line = direction_line[1]/direction_line[0] if direction_line[0] != 0 else np.inf
	slope_perpendicular = -1/slope_line if slope_line != 0 else np.inf

	start_perpendicular = point.get_center()

	if slope_perpendicular != np.inf:
		end_perpendicular = start_perpendicular + np.array([1, slope_perpendicular, 0])
	else:
		end_perpendicular = start_perpendicular + np.array([0, 1, 0])
	
	perpendicular_line = Line(start_perpendicular, end_perpendicular)

	intersection_point = intersection(line, perpendicular_line)

	return Dot(RIGHT * intersection_point[0] + UP * intersection_point[1], radius = 0.06, color = BLACK)

def project_point_to_line(dot, line):
    p = np.array(dot.get_center())
    a = np.array(line.get_start())
    b = np.array(line.get_end())

    ab = b - a
    ap = p - a

    projection = np.dot(ap, ab) / np.dot(ab, ab) * ab
    projection_point = a + projection

    return projection_point

def add_hash_mark(line, offset, n_hashes):
	angle = line.get_angle() + PI * 0.35
	hash_marks = VGroup()
	
	for i in range(n_hashes):
		pos = line.point_from_proportion(0.43 + (i + 1) / (n_hashes + 1) * 0.14)
		mark = Line(pos - offset * rotate_vector(RIGHT, angle), pos + offset * rotate_vector(RIGHT, angle),
					color=line.get_color(), stroke_width = 2)
		hash_marks.add(mark)
	
	return hash_marks

def get_dist(dot, line):
	p = np.array(dot.get_center())
	a = np.array(line.get_start())
	b = np.array(line.get_end())
	
	ab = b - a
	ap = p - a

	projection = np.dot(ap, ab) / np.dot(ab, ab) * ab

	d = ap - projection

	return np.linalg.norm(d)

def get_bisector(a, b, c):
	ba = b - a
	ca = c - a
	ba_unit = ba / np.linalg.norm(ba)
	ca_unit = ca / np.linalg.norm(ca)
	bisector_dir = ba_unit + ca_unit

	temp_l = a + bisector_dir

	return intersection(Line(a, temp_l), Line(b, c))


class TriangArea(Scene):
	def clearEverything(self):
		self.play(*[FadeOut(mob) for mob in self.mobjects])

	def showa1(self):
		p1 = Dot(2 * UP + 3 * LEFT, radius = 0.06, color = BLACK)
		p2 = Dot(2 * UP + 3 * RIGHT, radius = 0.06, color = BLACK)
		l1 = Line(p1.get_center(), p2.get_center(), color = RED)

		pa = Dot(1.25 * UP + 3.5 * LEFT, radius = 0.06, color = BLACK)
		pb = Dot(0.25 * UP + 3.5 * RIGHT, radius = 0.06, color = BLACK)
		pc = Dot(3 * DOWN + 1.5 * LEFT, radius = 0.06, color = BLACK)
		points = VGroup(pa, pb, pc)

		lab = Line(pa.get_center(), pb.get_center(), color = BLACK)
		lbc = Line(pb.get_center(), pc.get_center(), color = BLACK)
		lca = Line(pc.get_center(), pa.get_center(), color = BLACK)
		lines = VGroup(lab, lbc, lca)

		poly = Polygon(pa.get_center(), pb.get_center(), pc.get_center(), color = RED)
		poly.set_stroke(opacity = 0)
		poly.set_fill(RED, opacity = 0.7)
		poly.set_z_index(-1)

		self.wait(2)
		self.play(Create(p1), Create(p2), run_time = 2)
		self.play(Create(l1), run_time = 3)

		self.wait(2)
		self.play(Create(points, lag_ratio = 0), Create(lines, lag_ratio = 0), run_time = 2)
		self.play(FadeIn(poly), run_time = 4)

		self.wait(2)

	def showa2(self):
		grid = NumberPlane(x_range=[-1, 7, 1], y_range=[-1, 4, 1],
					 axis_config={"stroke_color": BLACK, "include_tip": True, "tip_length": 0.15, "tip_width": 0.1})\
						 .shift(2 * LEFT)

		rect = Rectangle(width=3, height=2, color=BLACK)
		rect.set_z_index(1)
		rect.move_to(grid.c2p(1.5, 1))
		a_label = Tex("a", color=BLACK).next_to(rect, LEFT)
		a_label.set_z_index(1)
		b_label = Tex("b", color=BLACK).next_to(rect, DOWN)
		b_label.set_z_index(1)

		txt1 = MathTex("S = a \cdot b", color = BLACK).next_to(grid, RIGHT).shift(1 * RIGHT + 1 * UP)

		txt2 = MathTex(r"S = 2 \cdot 3 = 6", color=BLACK).next_to(txt1, DOWN)

		checkers = VGroup()
		for x in range(3):
			for y in range(2):
				square = Square(side_length=1, color = BLACK)
				square.move_to(grid.c2p(x+0.5, y+0.5))
				square.set_fill(BLACK, 0.3)
				checkers.add(square)

		self.wait(2)
		self.play(Create(rect), run_time = 2)
		self.play(Write(a_label), Write(b_label), run_time = 2)
		self.wait(2)
		self.play(Write(txt1), run_time = 2)

		self.wait(2)
		self.play(Create(grid), run_time = 2)

		self.wait(2)
		self.play(Write(txt2), run_time = 2)

		self.wait(2)
		self.play(Create(checkers), run_time = 2)		

		self.wait(2)

	def showa3(self):
		pa = Dot(1.5 * UP + 1.5 * LEFT, radius = 0.06, color = BLACK)
		pb = Dot(1 * DOWN + 6 * LEFT, radius = 0.06, color = BLACK)
		pc = Dot(1.5 * DOWN + 0 * LEFT, radius = 0.06, color = BLACK)
		points = VGroup(pa, pb, pc)

		pa_t = Tex("A", color = BLACK).next_to(pa, UP).shift(0.15 * DOWN)
		pb_t = Tex("B", color = BLACK).next_to(pb, DOWN).shift(0.15 * UP)
		pc_t = Tex("C", color = BLACK).next_to(pc, DOWN).shift(0.15 * UP)
		points_t = VGroup(pa_t, pb_t, pc_t)

		lab = Line(pa.get_center(), pb.get_center(), color = BLACK)
		lbc = Line(pb.get_center(), pc.get_center(), color = BLACK)
		lca = Line(pc.get_center(), pa.get_center(), color = BLACK)
		lines = VGroup(lab, lbc, lca)

		lab_t = MathTex("c", color = BLACK).next_to(lab, UP).shift(1.3 * DOWN)
		lbc_t = MathTex("a", color = BLACK).next_to(lbc, DOWN).shift(0.4 * UP)
		lca_t = MathTex("b", color = BLACK).next_to(lca, RIGHT).shift(0.8 * LEFT)
		lines_t = VGroup(lab_t, lbc_t, lca_t)

		ph = find_foot_of_perpendicular(lbc, pa)
		ph_t = Tex("H", color = BLACK).next_to(ph, DOWN).shift(0.15 * UP)
		
		lah = Line(pa.get_center(), ph.get_center(), color = BLACK)
		lah_t = MathTex("h_a", color = BLACK).next_to(lah, RIGHT).shift(0.35 * LEFT + 0.5 * DOWN)

		ra = RightAngle(Line(ph.get_center(), pb.get_center()), Line(ph.get_center(), pa.get_center()),
				 length = 0.2, color = BLACK)

		txt1 = MathTex(r"S = \frac{1}{2} \cdot a \cdot h_a", color = BLACK).shift(3.5 * RIGHT + 2 * UP)

		pd = Dot(pb.get_center() + pa.get_center() - ph.get_center(), radius = 0.06, color = BLACK)
		pd_t = Tex("D", color = BLACK).next_to(pd, UP).shift(0.2 * DOWN)

		pe = Dot(pc.get_center() + pa.get_center() - ph.get_center(), radius = 0.06, color = BLACK)
		pe_t = Tex("E", color = BLACK).next_to(pe, UP).shift(0.2 * DOWN)

		lbd = Line(pb.get_center(), pd.get_center(), color = BLACK)
		lce = Line(pc.get_center(), pe.get_center(), color = BLACK)
		lde = Line(pd.get_center(), pe.get_center(), color = BLACK)

		mark1 = add_hash_mark(lah, 0.1, 1)
		mark2 = add_hash_mark(lbd, 0.1, 1)
		mark3 = add_hash_mark(lce, 0.1, 1)

		ra2 = RightAngle(Line(pb.get_center(), pd.get_center()), Line(pb.get_center(), ph.get_center()),
				   length = 0.2, color = BLACK)
		ra3 = RightAngle(Line(pc.get_center(), pe.get_center()), Line(pc.get_center(), ph.get_center()),
				   length = 0.2, color = BLACK)

		txt2 = MathTex(r"S_{BDEC} = a \cdot h_a", color = BLACK).shift(3.5 * RIGHT + 3 * UP)

		triang_bha = Polygon(pb.get_center(), ph.get_center(), pa.get_center(), stroke_opacity = 0,
					   fill_color = GREEN, fill_opacity = 0.5).set_z_index(-1)
		triang_bda = Polygon(pb.get_center(), pd.get_center(), pa.get_center(), stroke_opacity = 0,
					   fill_color = RED, fill_opacity = 0.5).set_z_index(-1)
		triang_cha = Polygon(pc.get_center(), ph.get_center(), pa.get_center(), stroke_opacity = 0,
					   fill_color = GREEN, fill_opacity = 0.5).set_z_index(-1)
		triang_cea = Polygon(pc.get_center(), pe.get_center(), pa.get_center(), stroke_opacity = 0,
					   fill_color = RED, fill_opacity = 0.5).set_z_index(-1)
		
		txt3 = MathTex(r"S_{BHA} = S_{BDA}", color = BLACK).next_to(txt2, DOWN).shift(0.3 * DOWN)
		txt4 = MathTex(r"S_{CHA} = S_{CEA}", color = BLACK).next_to(txt3, DOWN)

		txt5 = MathTex(r"S_{ABC} = S_{BHA} + S_{CHA} = \frac{1}{2} S_{BDEC}", font_size = 35, color = BLACK)\
			.next_to(txt4, DOWN)
		
		txt6 = MathTex(r"S_{ABC} = \frac{1}{2} a h_a", color = BLACK).next_to(txt5, DOWN).shift(0.2 * DOWN)
		sur_box_p1 = SurroundingRectangle(txt6).set_color(color_gradient([BLUE, YELLOW], 100)).set_stroke(width = 5)

		self.wait(2)
		self.play(Create(points, lag_ratio = 0), Write(points_t, lag_ratio = 0), Create(lines, lag_ratio = 0),
			Write(lines_t, lag_ratio = 0), run_time = 2)
		self.wait(2)
		self.play(Create(ph), Create(lah), Create(ra), Write(ph_t), Write(lah_t), run_time = 2)

		self.wait(2)
		self.play(Write(txt1), run_time = 2)
		self.wait(2)
		self.play(FadeOut(txt1), run_time = 2)

		self.wait(2)
		self.play(Create(pd), Create(pe), Write(pd_t), Write(pe_t), Create(lbd), Create(lce),Create(ra2),
		   Create(ra3), run_time = 2)
		self.play(Create(mark1), Create(mark2), Create(mark3), run_time = 2)
		self.wait(2)
		self.play(Create(lde), run_time = 2)

		self.wait(2)
		self.play(Write(txt2), run_time = 2)

		self.wait(2)
		self.play(FadeIn(triang_bha), run_time = 2)
		self.wait(2)
		self.play(FadeIn(triang_bda), run_time = 2)
		self.wait(2)
		self.play(Write(txt3), run_time = 2)

		self.wait(2)
		self.play(FadeIn(triang_cha), run_time = 2)
		self.wait(2)
		self.play(FadeIn(triang_cea), run_time = 2)
		self.wait(2)
		self.play(Write(txt4), run_time = 2)

		self.wait(2)
		self.play(Write(txt5), run_time = 2)
		self.wait(2)
		self.play(Write(txt6), run_time = 2)
		self.play(Create(sur_box_p1), run_time = 2)

		self.wait(3)
		self.play(FadeOut(ra3), FadeOut(txt2), FadeOut(txt3), FadeOut(txt4), FadeOut(txt5),
			txt6.animate.shift(3 * UP), sur_box_p1.animate.shift(3 * UP), run_time = 2)

		ang_a = Angle(Line(pc.get_center(), pa.get_center()), Line(pc.get_center(), pb.get_center()),
			   radius = 0.4, color = BLACK)
		ang_a_t = MathTex(r"\alpha", color = BLACK).next_to(ang_a, LEFT).shift(0.25 * RIGHT + 0.15 * UP)

		txt7 = MathTex(r"h_a = b \sin(\alpha)", color = BLACK).next_to(txt6, DOWN).shift(0.3 * DOWN)
		txt8 = MathTex(r"S_{ABC} = \frac{1}{2} a b \sin(\alpha)", color = BLACK).next_to(txt7, DOWN)\
			.shift(0.3 * DOWN)
		sur_box_p2 = SurroundingRectangle(txt8).set_color(color_gradient([BLUE, YELLOW], 100)).set_stroke(width = 5)

		self.wait(2)
		self.play(Create(ang_a), Write(ang_a_t), run_time = 2)
		self.wait(2)
		self.play(Write(txt7), run_time = 2)
		self.wait(2)
		self.play(Write(txt8), run_time = 2)
		self.play(Create(sur_box_p2), run_time = 2)

		self.wait(3)

	def showa4(self):
		pa = Dot(2.25 * UP + 4.5 * LEFT, radius = 0.06, color = BLACK)
		pb = Dot(1 * DOWN + 6.75 * LEFT, radius = 0.06, color = BLACK)
		pc = Dot(2 * DOWN + 3 * LEFT, radius = 0.06, color = BLACK)
		points = VGroup(pa, pb, pc)

		pa_t = Tex("A", color = BLACK).next_to(pa, UP).shift(0.15 * DOWN)
		pb_t = Tex("B", color = BLACK).next_to(pb, DOWN).shift(0.15 * UP)
		pc_t = Tex("C", color = BLACK).next_to(pc, DOWN).shift(0.15 * UP + 0.15 * LEFT)
		points_t = VGroup(pa_t, pb_t, pc_t)

		lab = Line(pa.get_center(), pb.get_center(), color = BLACK)
		lbc = Line(pb.get_center(), pc.get_center(), color = BLACK)
		lca = Line(pc.get_center(), pa.get_center(), color = BLACK)
		lines = VGroup(lab, lbc, lca)

		lab_t = MathTex("c", color = BLACK).next_to(lab, LEFT).shift(1.2 * RIGHT)
		lbc_t = MathTex("a", color = BLACK).next_to(lbc, DOWN).shift(0.6 * UP)
		lca_t = MathTex("b", color = BLACK).next_to(lca, RIGHT).shift(0.85 * LEFT)
		lines_t = VGroup(lab_t, lbc_t, lca_t)

		ang_a = Angle(Line(pc.get_center(), pa.get_center()), Line(pc.get_center(), pb.get_center()),
				radius = 0.4, color = BLACK)
		ang_a_t = MathTex(r"\alpha", color = BLACK).next_to(ang_a, LEFT).shift(0.35 * RIGHT + 0.2 * UP)

		txt1 = MathTex(r"S_{ABC} = \tfrac{1}{2} a b \sin(\alpha)", color = BLACK).shift(2.2 * RIGHT + 3.3 * UP)
		
		txt2 = MathTex(r"c^2 = a^2 + b^2 - 2ab\cos(\alpha)", color = BLACK).next_to(txt1, DOWN).shift(0.1 * DOWN)
		txt3 = MathTex(r"\cos(\alpha) = \tfrac{a^2 + b^2 - c^2}{2ab}", color = BLACK).next_to(txt2, DOWN)

		txt4 = MathTex(r"\sin^2(\alpha) = 1 - \cos^2(\alpha)", color = BLACK).next_to(txt3, DOWN).shift(0.1 * DOWN)
		txt5 = MathTex(r"\sin^2(\alpha) = (1 - \cos(\alpha))(1 + \cos(\alpha))", color = BLACK).next_to(txt4, DOWN)

		txt6 = MathTex(r"\sin^2(\alpha) = \frac{2ab - a^2 - b^2 + c^2}{2ab} \frac{2ab + a^2 + b^2 - c^2}{2ab}",
				font_size = 40, color = BLACK).next_to(txt5, DOWN).shift(0.2 * DOWN)

		self.wait(2)
		self.play(Create(points, lag_ratio = 0), Write(points_t, lag_ratio = 0), run_time = 2)
		self.play(Create(lines, lag_ratio = 0), Write(lines_t, lag_ratio = 0), run_time = 2)
		self.wait(2)
		self.play(Create(ang_a), Write(ang_a_t), run_time = 2)

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
		self.play(FadeOut(txt2), FadeOut(txt3), FadeOut(txt4), FadeOut(txt5), txt6.animate.shift(3.7 * UP),
			run_time = 2)

		txt7 = MathTex(r"\sin^2(\alpha) = \frac{c^2 - (a - b)^2}{2ab} \frac{(a + b)^2 - c^2}{2ab}", font_size = 40,
				color = BLACK).next_to(txt6, DOWN)
		txt8 = MathTex(r"\sin^2(\alpha) = \frac{(c - a + b)(c + a - b)(a + b - c)(a + b + c)}{4a^2b^2}",
				 font_size = 40, color = BLACK).next_to(txt7, DOWN)

		self.wait(2)
		self.play(Write(txt7), run_time = 2)
		self.wait(2)
		self.play(Write(txt8), run_time = 2)

		self.wait(2)
		self.play(FadeOut(txt6), FadeOut(txt7), txt8.animate.shift(2.3 * UP), run_time = 2)

		txt9 = MathTex(r"p = \frac{a + b + c}{2}", font_size = 40, color = BLACK).next_to(txt8, DOWN)\
			.shift(0.2 * DOWN)

		txt10 = MathTex(r"\sin^2(\alpha) = \frac{4}{4a^2b^2}(p - a)(p - b)(p - c)p", font_size = 40, color = BLACK)\
			.next_to(txt9, DOWN)

		txt11 = MathTex(r"\sin(\alpha) = \frac{2}{ab} \sqrt{(p - a)(p - b)(p - c)p}", font_size = 40,
				 color = BLACK).next_to(txt10, DOWN)

		self.wait(2)
		self.play(Write(txt9), run_time = 2)
		self.wait(2)
		self.play(Write(txt10), run_time = 2)
		self.wait(2)
		self.play(Write(txt11), run_time = 2)

		self.wait(2)
		self.play(FadeOut(txt8), FadeOut(txt10), txt9.animate.shift(1.5 * UP), txt11.animate.shift(2.7 * UP),
			run_time = 2)

		txt12 = MathTex(r"S_{ABC} = \frac{1}{2}ab\frac{2}{ab} \sqrt{(p - a)(p - b)(p - c)p}", font_size = 40,
				  color = BLACK).next_to(txt11, DOWN).shift(0.2 * DOWN)

		txt13 = MathTex(r"S_{ABC} = \sqrt{p(p - a)(p - b)(p - c)}", font_size = 40, color = BLACK)\
			.next_to(txt12, DOWN).shift(0.3 * DOWN)
		sur_box_p = SurroundingRectangle(txt13).set_color(color_gradient([BLUE, YELLOW], 100)).set_stroke(width = 5)

		self.wait(2)
		self.play(Write(txt12), run_time = 2)
		self.wait(2)
		self.play(Write(txt13), run_time = 2)
		self.play(Create(sur_box_p), run_time = 2)

		self.wait(3)

	def showa5(self):
		pa = Dot(2.5 * UP + 4 * LEFT, radius = 0.05, color = BLACK)
		pb = Dot(1 * DOWN + 6 * LEFT, radius = 0.05, color = BLACK)
		pc = Dot(2 * DOWN + 0 * LEFT, radius = 0.05, color = BLACK)
		points = VGroup(pa, pb, pc)

		pa_t = Tex("A", font_size = 40, color = BLACK).next_to(pa, UP).shift(0.15 * DOWN)
		pb_t = Tex("B", font_size = 40, color = BLACK).next_to(pb, DOWN).shift(0.15 * UP)
		pc_t = Tex("C", font_size = 40, color = BLACK).next_to(pc, DOWN).shift(0.15 * UP)
		points_t = VGroup(pa_t, pb_t, pc_t)

		lab = Line(pa.get_center(), pb.get_center(), color = BLACK, stroke_width = 2)
		lbc = Line(pb.get_center(), pc.get_center(), color = BLACK, stroke_width = 2)
		lca = Line(pc.get_center(), pa.get_center(), color = BLACK, stroke_width = 2)
		lines = VGroup(lab, lbc, lca)

		lab_t = MathTex("c", color = BLACK).next_to(lab, LEFT).shift(1.05 * RIGHT)
		lbc_t = MathTex("a", color = BLACK).next_to(lbc, DOWN).shift(0.6 * UP)
		lca_t = MathTex("b", color = BLACK).next_to(lca, RIGHT).shift(2.0 * LEFT)
		lines_t = VGroup(lab_t, lbc_t, lca_t)

		pl1 = get_bisector(pa.get_center(), pb.get_center(), pc.get_center())
		lal1 = Line(pa.get_center(), pl1, color = BLACK)
		pl2 = get_bisector(pb.get_center(), pc.get_center(), pa.get_center())
		lal2 = Line(pb.get_center(), pl2, color = BLACK)

		po = Dot(intersection(lal1, lal2), radius = 0.05, color = BLACK)
		po_t = Tex("O", font_size = 40, color = BLACK).next_to(po, DOWN).shift(0.1 * UP + 0.15 * RIGHT)

		r_val = get_dist(po, lab)

		circ = Circle(radius = r_val, color = BLACK, stroke_width = 2).move_to(po.get_center())

		loa = Line(po.get_center(), pa.get_center(), color = BLACK, stroke_width = 2)
		lob = Line(po.get_center(), pb.get_center(), color = BLACK, stroke_width = 2)
		loc = Line(po.get_center(), pc.get_center(), color = BLACK, stroke_width = 2)
		lines2 = VGroup(loa, lob, loc)

		p_o_ab_proj = project_point_to_line(po, lab)
		lo_ab = Line(po.get_center(), p_o_ab_proj, color = BLACK, stroke_width = 2)
		lo_ab_t = MathTex("r", color = BLACK).next_to(lo_ab, UP).shift(0.5 * DOWN)
		ra1 = RightAngle(Line(p_o_ab_proj, po.get_center()), Line(p_o_ab_proj, pa.get_center()), length = 0.2,
				   color = BLACK)

		p_o_bc_proj = project_point_to_line(po, lbc)
		lo_bc = Line(po.get_center(), p_o_bc_proj, color = BLACK, stroke_width = 2)
		lo_bc_t = MathTex("r", color = BLACK).next_to(lo_bc, LEFT).shift(0.3 * RIGHT)
		ra2 = RightAngle(Line(p_o_bc_proj, po.get_center()), Line(p_o_bc_proj, pb.get_center()), length = 0.2,
				   color = BLACK)
		
		p_o_ca_proj = project_point_to_line(po, lca)
		lo_ca = Line(po.get_center(), p_o_ca_proj, color = BLACK, stroke_width = 2)
		lo_ca_t = MathTex("r", color = BLACK).next_to(lo_ca, DOWN).shift(0.6 * UP)
		ra3 = RightAngle(Line(p_o_ca_proj, po.get_center()), Line(p_o_ca_proj, pc.get_center()), length = 0.2,
				   color = BLACK)

		txt1 = MathTex(r"S_{ABC} = S_{AOB} + S_{BOC} + S_{COA}", font_size = 40, color = BLACK)\
			.shift(3.5 * RIGHT + 3 * UP)

		txt2 = MathTex(r"S_{AOB} = \tfrac{1}{2} c r", font_size = 40, color = BLACK).next_to(txt1, DOWN)\
			.shift(0.2 * LEFT)
		txt3 = MathTex(r"S_{BOC} = \tfrac{1}{2} a r", font_size = 40, color = BLACK).next_to(txt2, DOWN)
		txt4 = MathTex(r"S_{COA} = \tfrac{1}{2} b r", font_size = 40, color = BLACK).next_to(txt3, DOWN)

		txt5 = MathTex(r"S_{ABC} = \tfrac{1}{2} a r + \tfrac{1}{2} b r + \tfrac{1}{2} c r", font_size = 40,
				color = BLACK).next_to(txt4, DOWN).shift(0.1 * DOWN)
		txt6 = MathTex(r"S_{ABC} = \tfrac{1}{2} (a + b + c) r", font_size = 40, color = BLACK).next_to(txt5, DOWN)

		txt7 = MathTex(r"p = \tfrac{a + b + c}{2}", font_size = 40, color = BLACK).next_to(txt6, DOWN)

		txt8 = MathTex(r"S_{ABC} = p r", font_size = 50, color = BLACK).next_to(txt7, DOWN).shift(0.2 * DOWN)

		sur_box_p = SurroundingRectangle(txt8).set_color(color_gradient([BLUE, YELLOW], 100)).set_stroke(width = 5)

		self.wait(2)
		self.play(Create(points, lag_ratio = 0), Write(points_t, lag_ratio = 0), Create(lines, lag_ratio = 0),
			Write(lines_t, lag_ratio = 0), run_time = 2)
		self.wait(2)
		self.play(Create(po), Write(po_t), Create(circ), run_time = 2)

		self.wait(2)
		self.play(Create(lines2, lag_ratio = 0), run_time = 2)
		self.wait(2)
		self.play(Create(lo_ab), Create(ra1), Write(lo_ab_t), run_time = 2)
		self.play(Create(lo_bc), Create(ra2), Write(lo_bc_t), run_time = 2)
		self.play(Create(lo_ca), Create(ra3), Write(lo_ca_t), run_time = 2)

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
		self.play(Write(txt7), run_time = 2)
		self.wait(2)
		self.play(Write(txt8), run_time = 2)
		self.play(Create(sur_box_p), run_time = 2)

		self.wait(2)

	def showa6(self):
		pa = Dot(2.5 * UP + 4 * LEFT, radius = 0.05, color = BLACK)
		pb = Dot(1 * DOWN + 6 * LEFT, radius = 0.05, color = BLACK)
		pc = Dot(2 * DOWN + 0 * LEFT, radius = 0.05, color = BLACK)
		points = VGroup(pa, pb, pc)

		pa_t = Tex("A", font_size = 40, color = BLACK).next_to(pa, UP).shift(0.15 * DOWN)
		pb_t = Tex("B", font_size = 40, color = BLACK).next_to(pb, DOWN).shift(0.15 * UP)
		pc_t = Tex("C", font_size = 40, color = BLACK).next_to(pc, DOWN).shift(0.15 * UP)
		points_t = VGroup(pa_t, pb_t, pc_t)

		lab = Line(pa.get_center(), pb.get_center(), color = BLACK, stroke_width = 2)
		lbc = Line(pb.get_center(), pc.get_center(), color = BLACK, stroke_width = 2)
		lca = Line(pc.get_center(), pa.get_center(), color = BLACK, stroke_width = 2)
		lines = VGroup(lab, lbc, lca)

		lab_t = MathTex("c", color = BLACK).next_to(lab, LEFT).shift(1.05 * RIGHT)
		lbc_t = MathTex("a", color = BLACK).next_to(lbc, DOWN).shift(0.6 * UP)
		lca_t = MathTex("b", color = BLACK).next_to(lca, RIGHT).shift(2.0 * LEFT)
		lines_t = VGroup(lab_t, lbc_t, lca_t)

		pl1 = get_bisector(pa.get_center(), pb.get_center(), pc.get_center())
		lal1 = Line(pa.get_center(), pl1, color = BLACK)
		pl2 = get_bisector(pb.get_center(), pc.get_center(), pa.get_center())
		lal2 = Line(pb.get_center(), pl2, color = BLACK)

		po = Dot(intersection(lal1, lal2), radius = 0.05, color = BLACK)
		po_t = Tex("O", font_size = 40, color = BLACK).next_to(po, DOWN).shift(0.2 * UP + 0.15 * RIGHT)

		r_val = get_dist(po, lab)

		circ = Circle(radius = r_val, color = BLACK, stroke_width = 2).move_to(po.get_center())

		p_o_ca_proj = project_point_to_line(po, lca)
		lo_ca = Line(po.get_center(), p_o_ca_proj, color = BLACK, stroke_width = 2)
		lo_ca_t = MathTex("r", color = BLACK).next_to(lo_ca, DOWN).shift(0.6 * UP)

		ph = Dot(find_foot_of_perpendicular(lbc, pa).get_center(), radius = 0.05, color = BLACK)
		ph_t = Tex("H", font_size = 40, color = BLACK).next_to(ph, DOWN).shift(0.2 * UP)

		lah = Line(pa.get_center(), ph.get_center(), color = BLACK, stroke_width = 2)
		lah_t = MathTex("h_a", color = BLACK, font_size = 40).next_to(lah, RIGHT).shift(0.5 * LEFT)

		txt1 = MathTex(r"S_{ABC} = \frac{1}{2} a h_a", font_size = 50, color = BLACK)\
			.shift(3.5 * RIGHT + 2.5 * UP)
		sur_box_p1 = SurroundingRectangle(txt1).set_color(color_gradient([BLUE, YELLOW], 100)).set_stroke(width = 5)

		txt2 = MathTex(r"S_{ABC} = \frac{1}{2} a b \sin(\alpha)", font_size = 50, color = BLACK)\
			.next_to(txt1, DOWN).shift(0.2 * DOWN)
		sur_box_p2 = SurroundingRectangle(txt2).set_color(color_gradient([BLUE, YELLOW], 100)).set_stroke(width = 5)

		txt3 = MathTex(r"p = \tfrac{a + b + c}{2}", font_size = 50, color = BLACK).next_to(txt2, DOWN)\
			.shift(0.2 * DOWN)

		txt4 = MathTex(r"S_{ABC} = \sqrt{p (p - a) (p - b) (p - c)}", font_size = 40, color = BLACK)\
			.next_to(txt3, DOWN).shift(0.2 * DOWN)
		sur_box_p4 = SurroundingRectangle(txt4).set_color(color_gradient([BLUE, YELLOW], 100)).set_stroke(width = 5)

		txt5 = MathTex(r"S_{ABC} = r p", font_size = 50, color = BLACK).next_to(txt4, DOWN).shift(0.2 * DOWN)
		sur_box_p5 = SurroundingRectangle(txt5).set_color(color_gradient([BLUE, YELLOW], 100)).set_stroke(width = 5)

		self.wait(2)
		self.play(Create(points, lag_ratio = 0), Write(points_t, lag_ratio = 0), Create(lines, lag_ratio = 0),
			Write(lines_t, lag_ratio = 0), run_time = 2)
		self.wait(2)
		self.play(Create(ph), Create(lah), Write(ph_t), Write(lah_t), run_time = 2)
		self.wait(2)
		self.play(Create(po), Write(po_t), Create(circ), run_time = 2)
		self.play(Create(lo_ca), Write(lo_ca_t), run_time = 2)

		self.wait(2)
		self.play(Write(txt1), run_time = 2)
		self.play(Create(sur_box_p1), run_time = 2)
		self.wait(2)
		self.play(Write(txt2), run_time = 2)
		self.play(Create(sur_box_p2), run_time = 2)
		self.wait(2)
		self.play(Write(txt3), run_time = 2)
		self.wait(2)
		self.play(Write(txt4), run_time = 2)
		self.play(Create(sur_box_p4), run_time = 2)
		self.wait(2)
		self.play(Write(txt5), run_time = 2)
		self.play(Create(sur_box_p5), run_time = 2)

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
		self.showa5()
		self.clearEverything()
		self.showa6()
		self.clearEverything()