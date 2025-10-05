import open3d as o3d
import os
import glob

def display_and_save_pointclouds(directory, image_prefix="frame", width=600, height=1080):
    
    # Get all .ply files in the directory
    pointcloud_files = glob.glob(os.path.join(directory, "*.ply"))
    
    # Initialize visualizer
    vis = o3d.visualization.Visualizer()
    vis.create_window(width=width, height=height)

    render_option = vis.get_render_option()
    render_option.lighting_profile = o3d.visualization.RenderOption.LightingProfile.HARD_SHADOWS  # Options: NO_SHADOWS, HARD_SHADOWS, SOFT_SHADOWS
    render_option.background_color = [0.1, 0.1, 0.1]  # Set background to a darker color for better lighting contrast

    output_image_directory = f"D:\\studia\doktorat\\segmentation\\data\\publikacja\\skrajnie_otyla_sylwetka\\results_before_train\\SPRING2277\\aggs"

    # Loop through each point cloud file
    for idx, file in enumerate(pointcloud_files):
        # Load the point cloud
        pcd = o3d.io.read_triangle_mesh(file, True)

        # Clear geometry and add new point cloud
        vis.clear_geometries()
        vis.add_geometry(pcd)

        view_ctl = vis.get_view_control()


        #back
        view_ctl.rotate(0,-500.0, 200)  # Rotate the camera
        vis.poll_events()
        vis.update_renderer()
        vis.capture_screen_image(f"{output_image_directory}/{image_prefix}_{idx:04d}.png")

        # #front
        # view_ctl.rotate(-1000.0, 0.0)  # Rotate the camera
        # vis.poll_events()
        # vis.update_renderer()
        # vis.capture_screen_image(f"{output_image_directory_f}/{image_prefix}_{idx:04d}.png")

        # # #side
        # view_ctl.rotate(-500.0, 0.0)  # Rotate the camera
        # vis.poll_events()
        # vis.update_renderer()
        # vis.capture_screen_image(f"{output_image_directory_s}/{image_prefix}_{idx:04d}.png")

        # # #perspective
        # view_ctl.rotate(750.0, 75.0)  # Rotate the camera
        # view_ctl.translate(0, 50.0)  # Translate the camera slightly (X and Y)
        # vis.poll_events()
        # vis.update_renderer()
        # vis.capture_screen_image(f"{output_image_directory_p}/{image_prefix}_{idx:04d}.png")
        
        # Modify camera parameters (adjust these for your preferred angle)
        #view_ctl.rotate(-250.0, 75.0)  # Rotate the camera
        #view_ctl.translate(0, 50.0)  # Translate the camera slightly (X and Y)

        #view_ctl.rotate(-500.0, 0.0)  # Rotate the camera
        #view_ctl.translate(0, 0.0)  # Translate the camera slightly (X and Y)

        # Update the visualizer and capture the frame
        # vis.poll_events()
        # vis.update_renderer()

        # # Save the frame as an image
        # vis.capture_screen_image(f"{output_image_directory_b}/{image_prefix}_{idx:04d}.png")
    
    vis.destroy_window()

    print(f"Saved {len(pointcloud_files)} frames to {output_image_directory_b}.")
    
# Example usage:
if __name__ == "__main__":
    # Directory containing point clouds

    directory =  "D:\\studia\doktorat\\segmentation\\data\\publikacja\\skrajnie_otyla_sylwetka\\results_before_train\\SPRING2277\\aggs"


    display_and_save_pointclouds(directory)