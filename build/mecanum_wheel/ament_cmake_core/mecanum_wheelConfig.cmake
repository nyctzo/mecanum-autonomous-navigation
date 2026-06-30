# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_mecanum_wheel_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED mecanum_wheel_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(mecanum_wheel_FOUND FALSE)
  elseif(NOT mecanum_wheel_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(mecanum_wheel_FOUND FALSE)
  endif()
  return()
endif()
set(_mecanum_wheel_CONFIG_INCLUDED TRUE)

# output package information
if(NOT mecanum_wheel_FIND_QUIETLY)
  message(STATUS "Found mecanum_wheel: 0.1.0 (${mecanum_wheel_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'mecanum_wheel' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT mecanum_wheel_DEPRECATED_QUIET)
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(mecanum_wheel_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${mecanum_wheel_DIR}/${_extra}")
endforeach()
