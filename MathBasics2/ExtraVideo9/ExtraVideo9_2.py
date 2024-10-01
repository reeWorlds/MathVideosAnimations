from manim import *


class ExtraVid9_2(Scene):
	def clearEverything(self):
		self.play(*[FadeOut(mob) for mob in self.mobjects])

	def showa1(self):
		axes = Axes(
			x_range=[-3.25, 1.25, 1],
			y_range=[-1.5, 4.5, 1],
			x_length=4,
			y_length=6,
			axis_config={"color": BLACK, "stroke_width": 8},
			x_axis_config={"unit_size": 0.9},
			y_axis_config={"unit_size": 0.9}
		).shift(0.4)

		x_label = axes.get_x_axis_label("x", direction=RIGHT, buff=0.12).set_color(BLACK)
		y_label = axes.get_y_axis_label("a", direction=UP, buff=0.22).set_color(BLACK)
		one_label = MathTex("1", color=BLACK, font_size=42).next_to(axes.c2p(0, 1), RIGHT)\
			.shift(UP * 0.25 + LEFT * 0.1)

		self.wait(2)
		self.play(Create(axes), run_time=2)
		self.play(Write(x_label), Write(y_label), Write(one_label), run_time=1)
		self.wait(4)

		RDC = "#CF0000"
		opc = 0.15
		stw = 4

		line1_1 = Line(start=axes.c2p(0, -1.5), end=axes.c2p(0, 4.5), color=RDC, stroke_width=stw)
		line1_2 = Line(start=axes.c2p(-3.25, 0), end=axes.c2p(1.25, 0), color=RDC, stroke_width=stw)
		r12bl = axes.c2p(-3.25, -1.5)
		r12tr = axes.c2p(1.25, 0)
		rect1_2 = Rectangle(height=r12tr[1]-r12bl[1], width=r12tr[0]-r12bl[0], fill_color=RED,
					  fill_opacity=opc, stroke_width=0)
		rect1_2.move_to(r12bl + (r12tr - r12bl) / 2)
		line1_3 = Line(start=axes.c2p(-3.25, 2), end=axes.c2p(1.25, 2), color=RDC, stroke_width=stw)

		self.play(Create(line1_1), run_time=1)
		self.wait(2)
		self.play(Create(line1_2), run_time=1)
		self.play(FadeIn(rect1_2, direction=UP), run_time=1)
		self.wait(2)
		self.play(Create(line1_3), run_time=1)
		self.wait(4)

		line2_1 = Line(start=axes.c2p(-3.25, -1.25), end=axes.c2p(1.25, 3.25), color=RDC, stroke_width=stw)
		line2_2 = Line(start=axes.c2p(-3.25, 1), end=axes.c2p(1.25, 1), color=RDC, stroke_width=stw)
		r22bl = axes.c2p(-3.25, -1.5)
		r22tr = axes.c2p(1.25, 1)
		rect2_2 = Rectangle(height=r22tr[1]-r22bl[1], width=r22tr[0]-r22bl[0], fill_color=RED,
					  fill_opacity=opc, stroke_width=0)
		rect2_2.move_to(r22bl + (r22tr - r22bl) / 2)

		self.play(Create(line2_1), run_time=1)
		self.wait(2)
		self.play(Create(line2_2), run_time=1)
		self.play(FadeIn(rect2_2, direction=UP), run_time=1)
		self.wait(4)

		line3_1 = DashedLine(start=axes.c2p(-2, -1.5), end=axes.c2p(-2, 4.5), dash_length=0.15,
					   dashed_ratio=0.5, color=RDC, stroke_width=stw)
		r31bl = axes.c2p(-3.25, -1.5)
		r31tr = axes.c2p(-2, 4.5)
		rect3_1 = Rectangle(height=r31tr[1]-r31bl[1], width=r31tr[0]-r31bl[0], fill_color=RED,
					  fill_opacity=opc, stroke_width=0)
		rect3_1.move_to(r31bl + (r31tr - r31bl) / 2)
		r32bl = axes.c2p(0, -1.5)
		r32tr = axes.c2p(1.25, 4.5)
		rect3_2 = Rectangle(height=r32tr[1]-r32bl[1], width=r32tr[0]-r32bl[0], fill_color=RED,
					  fill_opacity=opc, stroke_width=0)
		rect3_2.move_to(r32bl + (r32tr - r32bl) / 2)

		self.play(Create(line3_1), run_time=1)
		self.play(FadeIn(rect3_1, direction=UP), run_time=1)
		self.wait(2)
		self.play(FadeIn(rect3_2), run_time=1)
		self.wait(4)

		p_opc = 0.4

		blue_verts = [axes.c2p(-1, 1), axes.c2p(0, 2), axes.c2p(0, 1)]
		blue_poly = Polygon(*blue_verts, fill_color=BLUE, fill_opacity=p_opc, stroke_width=0)
		green_verts = [axes.c2p(-2, 1), axes.c2p(-2, 2), axes.c2p(0, 2), axes.c2p(-1, 1)]
		green_poly = Polygon(*green_verts, fill_color=GREEN, fill_opacity=p_opc, stroke_width=0)
		yellow_verts = [axes.c2p(-2, 2), axes.c2p(-2, 4.5), axes.c2p(0, 4.5), axes.c2p(0, 2)]
		yellow_poly = Polygon(*yellow_verts, fill_color=YELLOW, fill_opacity=p_opc, stroke_width=0)

		self.play(FadeIn(blue_poly, direction=UP), run_time=0.5)
		self.play(FadeIn(green_poly, direction=UP), run_time=0.5)
		self.play(FadeIn(yellow_poly, direction=UP), run_time=0.5)
		self.wait(4)

		line4_1 = DashedLine(start=axes.c2p(-1, 1), end=axes.c2p(0, 1.5), dash_length=0.2,
					   dashed_ratio=0.75, color=RDC, stroke_width=stw)
		verts4_2 = [axes.c2p(-1, 1), axes.c2p(0, 1.5), axes.c2p(0, 1)]
		poly4_2 = Polygon(*verts4_2, fill_color=RED, fill_opacity=opc, stroke_width=0)

		self.play(FadeOut(blue_poly), run_time=1)
		self.wait(2)
		self.play(Create(line4_1), run_time=1)
		self.play(FadeIn(poly4_2, direction=UP), run_time=1)
		self.wait(4)

		line5_1 = DashedLine(start=axes.c2p(-1, 1), end=axes.c2p(-1, 2), dash_length=0.15,
					   dashed_ratio=0.5, color=RDC, stroke_width=stw)
		verts5_2 = [axes.c2p(-1, 1), axes.c2p(-1, 2), axes.c2p(-2, 2), axes.c2p(-2, 1)]
		poly5_2 = Polygon(*verts5_2, fill_color=RED, fill_opacity=opc, stroke_width=0)

		self.play(FadeOut(green_poly), run_time=1)
		self.wait(2)
		self.play(Create(line5_1), run_time=1)
		self.play(FadeIn(poly5_2, direction=UP), run_time=1)
		self.wait(4)

		line6_1 = DashedLine(start=axes.c2p(-1, 2), end=axes.c2p(-1, 4.5), dash_length=0.15,
					   dashed_ratio=0.5, color=RDC, stroke_width=stw)
		verts6_2 = [axes.c2p(-1, 2), axes.c2p(-1, 4.5), axes.c2p(0, 4.5), axes.c2p(0, 2)]
		poly6_2 = Polygon(*verts6_2, fill_color=RED, fill_opacity=opc, stroke_width=0)

		self.play(FadeOut(yellow_poly), run_time=1)
		self.wait(2)
		self.play(Create(line6_1), run_time=1)
		self.play(FadeIn(poly6_2, direction=UP), run_time=1)
		self.wait(4)

		y_line = ValueTracker(-0.75)
		hor_line = always_redraw(lambda: Line(start=axes.c2p(-3.25, y_line.get_value()),
								end=axes.c2p(1.25, y_line.get_value()), color=BLACK, stroke_width=2.5))

		self.play(Create(hor_line), run_time=1)
		self.wait(3)
		self.play(y_line.animate.set_value(1.3), run_time=1)
		self.wait(3)
		self.play(y_line.animate.set_value(1.75), run_time=1)
		self.wait(3)
		self.play(y_line.animate.set_value(3.25), run_time=1)
		self.wait(3)
		self.play(y_line.animate.set_value(0.5), run_time=1)
		self.wait(6)

	def construct(self):
		self.camera.background_color = WHITE

		self.showa1()
		self.clearEverything()
