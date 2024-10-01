import bpy

# Clear existing objects, except for cameras and lights
for obj in bpy.context.scene.objects:
    if obj.type not in {'CAMERA', 'LIGHT'}:
        obj.select_set(True)
    else:
        obj.select_set(False)
bpy.ops.object.delete()

# Function to create a material
def create_material(name, color, opacity):
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    principled_node = nodes.get('Principled BSDF')
    principled_node.inputs['Base Color'].default_value = (*color, 1)
    principled_node.inputs['Alpha'].default_value = opacity
    mat.blend_method = 'BLEND' if opacity < 1.0 else 'OPAQUE'
    return mat

def mark_freestyle_edges(obj, mark_seams=True):
    # Enter Edit Mode
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.mode_set(mode='EDIT')
    
    # Select all edges
    bpy.ops.mesh.select_all(action='SELECT')
    
    # Mark as Freestyle Edge
    bpy.ops.mesh.mark_freestyle_edge(clear=False)
    
    # Optionally, mark seams for better edge detection
    if mark_seams:
        bpy.ops.mesh.mark_seam(clear=False)
    
    # Return to Object Mode
    bpy.ops.object.mode_set(mode='OBJECT')

# Function to create a cone
def create_cone(radius, depth, location, color, opacity):
    bpy.ops.mesh.primitive_cone_add(radius1=radius, depth=depth, location=location, vertices=256)
    cone_obj = bpy.context.active_object
    cone_mat = create_material("ConeMaterial", color, opacity)
    cone_obj.data.materials.append(cone_mat)
    mark_freestyle_edges(cone_obj)

# Function to create a cylinder
def create_cylinder(radius, depth, location, material):
    bpy.ops.mesh.primitive_cylinder_add(radius=radius, depth=depth, location=location, vertices=256)
    cylinder_obj = bpy.context.active_object
    cylinder_obj.data.materials.append(material)
    mark_freestyle_edges(cylinder_obj)

# Set up scene for Freestyle rendering
bpy.context.scene.render.use_freestyle = True
bpy.context.scene.render.engine = 'CYCLES'
view_layer = bpy.context.view_layer
freestyle = view_layer.freestyle_settings
freestyle.linesets.new(name="FreestyleLineSet")

# Configure Freestyle lineset
lineset = freestyle.linesets["FreestyleLineSet"]
lineset.select_by_visibility = True
lineset.select_by_edge_types = True
lineset.select_silhouette = True
lineset.select_border = True
lineset.select_crease = True
lineset.select_ridge_valley = True
lineset.select_suggestive_contour = True

# Get the linestyle associated with the lineset
linestyle = bpy.data.linestyles[lineset.linestyle.name]
linestyle.color = (0, 0, 0.75)  # Set the line color to blue
linestyle.thickness = 1  # Increase thickness for better visibility

# Create objects with materials
cone_radius = 1
cone_depth = 4
cone_color = (0, 0.75, 0)  # Dark Green
cone_opacity = 0.7
create_cone(cone_radius, cone_depth, (0, 0, cone_depth / 2), cone_color, cone_opacity)

cylinder_material = create_material("CylinderMaterial", (0, 0, 0.75), 0.35)  # Blue

n_cyls = 15
cyl_h = cone_depth / n_cyls

# Create cylinders at different heights
for i in range(n_cyls):
    z_pos = i * cyl_h + cyl_h / 2
    cyl_r = cone_radius * (1 - (i / n_cyls))
    create_cylinder(cyl_r + 1e-4, cyl_h - 1e-4, (0, 0, z_pos), cylinder_material)
