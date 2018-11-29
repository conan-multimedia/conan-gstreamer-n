from conans import ConanFile, tools
import os

class GstreamerConan(ConanFile):
    name = "gstreamer"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"
    description = "<Description of Gstreamer here>"
    url = "None"
    license = "None"

    def build(self):
        pkg_config_path = os.path.normpath(os.getcwd()+'/../lib/pkgconfig/')
        #print os.getcwd(), pkg_config_path
        pc_list = os.listdir(pkg_config_path)
        for pc in pc_list:
            tools.replace_prefix_in_pc_file_full(os.path.join(pkg_config_path,pc), '${gstreamer_root}')


    def package(self):
        self.copy("*")

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
