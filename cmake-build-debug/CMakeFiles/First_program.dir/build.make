# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /home/atmadeep/clion-2018.1.6/bin/cmake/bin/cmake

# The command to remove a file.
RM = /home/atmadeep/clion-2018.1.6/bin/cmake/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/atmadeep/CLionProjects/Image_Processing

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/atmadeep/CLionProjects/Image_Processing/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/First_program.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/First_program.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/First_program.dir/flags.make

CMakeFiles/First_program.dir/First_program.cpp.o: CMakeFiles/First_program.dir/flags.make
CMakeFiles/First_program.dir/First_program.cpp.o: ../First_program.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/atmadeep/CLionProjects/Image_Processing/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/First_program.dir/First_program.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/First_program.dir/First_program.cpp.o -c /home/atmadeep/CLionProjects/Image_Processing/First_program.cpp

CMakeFiles/First_program.dir/First_program.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/First_program.dir/First_program.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/atmadeep/CLionProjects/Image_Processing/First_program.cpp > CMakeFiles/First_program.dir/First_program.cpp.i

CMakeFiles/First_program.dir/First_program.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/First_program.dir/First_program.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/atmadeep/CLionProjects/Image_Processing/First_program.cpp -o CMakeFiles/First_program.dir/First_program.cpp.s

CMakeFiles/First_program.dir/First_program.cpp.o.requires:

.PHONY : CMakeFiles/First_program.dir/First_program.cpp.o.requires

CMakeFiles/First_program.dir/First_program.cpp.o.provides: CMakeFiles/First_program.dir/First_program.cpp.o.requires
	$(MAKE) -f CMakeFiles/First_program.dir/build.make CMakeFiles/First_program.dir/First_program.cpp.o.provides.build
.PHONY : CMakeFiles/First_program.dir/First_program.cpp.o.provides

CMakeFiles/First_program.dir/First_program.cpp.o.provides.build: CMakeFiles/First_program.dir/First_program.cpp.o


# Object files for target First_program
First_program_OBJECTS = \
"CMakeFiles/First_program.dir/First_program.cpp.o"

# External object files for target First_program
First_program_EXTERNAL_OBJECTS =

First_program: CMakeFiles/First_program.dir/First_program.cpp.o
First_program: CMakeFiles/First_program.dir/build.make
First_program: /usr/local/lib/libopencv_stitching.so.3.4.1
First_program: /usr/local/lib/libopencv_superres.so.3.4.1
First_program: /usr/local/lib/libopencv_videostab.so.3.4.1
First_program: /usr/local/lib/libopencv_aruco.so.3.4.1
First_program: /usr/local/lib/libopencv_bgsegm.so.3.4.1
First_program: /usr/local/lib/libopencv_bioinspired.so.3.4.1
First_program: /usr/local/lib/libopencv_ccalib.so.3.4.1
First_program: /usr/local/lib/libopencv_cvv.so.3.4.1
First_program: /usr/local/lib/libopencv_dnn_objdetect.so.3.4.1
First_program: /usr/local/lib/libopencv_dpm.so.3.4.1
First_program: /usr/local/lib/libopencv_face.so.3.4.1
First_program: /usr/local/lib/libopencv_freetype.so.3.4.1
First_program: /usr/local/lib/libopencv_fuzzy.so.3.4.1
First_program: /usr/local/lib/libopencv_hdf.so.3.4.1
First_program: /usr/local/lib/libopencv_hfs.so.3.4.1
First_program: /usr/local/lib/libopencv_img_hash.so.3.4.1
First_program: /usr/local/lib/libopencv_line_descriptor.so.3.4.1
First_program: /usr/local/lib/libopencv_optflow.so.3.4.1
First_program: /usr/local/lib/libopencv_reg.so.3.4.1
First_program: /usr/local/lib/libopencv_rgbd.so.3.4.1
First_program: /usr/local/lib/libopencv_saliency.so.3.4.1
First_program: /usr/local/lib/libopencv_sfm.so.3.4.1
First_program: /usr/local/lib/libopencv_stereo.so.3.4.1
First_program: /usr/local/lib/libopencv_structured_light.so.3.4.1
First_program: /usr/local/lib/libopencv_surface_matching.so.3.4.1
First_program: /usr/local/lib/libopencv_tracking.so.3.4.1
First_program: /usr/local/lib/libopencv_xfeatures2d.so.3.4.1
First_program: /usr/local/lib/libopencv_ximgproc.so.3.4.1
First_program: /usr/local/lib/libopencv_xobjdetect.so.3.4.1
First_program: /usr/local/lib/libopencv_xphoto.so.3.4.1
First_program: /usr/local/lib/libopencv_photo.so.3.4.1
First_program: /usr/local/lib/libopencv_shape.so.3.4.1
First_program: /usr/local/lib/libopencv_calib3d.so.3.4.1
First_program: /usr/local/lib/libopencv_viz.so.3.4.1
First_program: /usr/local/lib/libopencv_phase_unwrapping.so.3.4.1
First_program: /usr/local/lib/libopencv_video.so.3.4.1
First_program: /usr/local/lib/libopencv_datasets.so.3.4.1
First_program: /usr/local/lib/libopencv_plot.so.3.4.1
First_program: /usr/local/lib/libopencv_text.so.3.4.1
First_program: /usr/local/lib/libopencv_dnn.so.3.4.1
First_program: /usr/local/lib/libopencv_features2d.so.3.4.1
First_program: /usr/local/lib/libopencv_flann.so.3.4.1
First_program: /usr/local/lib/libopencv_highgui.so.3.4.1
First_program: /usr/local/lib/libopencv_ml.so.3.4.1
First_program: /usr/local/lib/libopencv_videoio.so.3.4.1
First_program: /usr/local/lib/libopencv_imgcodecs.so.3.4.1
First_program: /usr/local/lib/libopencv_objdetect.so.3.4.1
First_program: /usr/local/lib/libopencv_imgproc.so.3.4.1
First_program: /usr/local/lib/libopencv_core.so.3.4.1
First_program: CMakeFiles/First_program.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/atmadeep/CLionProjects/Image_Processing/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable First_program"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/First_program.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/First_program.dir/build: First_program

.PHONY : CMakeFiles/First_program.dir/build

CMakeFiles/First_program.dir/requires: CMakeFiles/First_program.dir/First_program.cpp.o.requires

.PHONY : CMakeFiles/First_program.dir/requires

CMakeFiles/First_program.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/First_program.dir/cmake_clean.cmake
.PHONY : CMakeFiles/First_program.dir/clean

CMakeFiles/First_program.dir/depend:
	cd /home/atmadeep/CLionProjects/Image_Processing/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/atmadeep/CLionProjects/Image_Processing /home/atmadeep/CLionProjects/Image_Processing /home/atmadeep/CLionProjects/Image_Processing/cmake-build-debug /home/atmadeep/CLionProjects/Image_Processing/cmake-build-debug /home/atmadeep/CLionProjects/Image_Processing/cmake-build-debug/CMakeFiles/First_program.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/First_program.dir/depend
