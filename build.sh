cd ~/workspace/cerbero/build/dist/linux_x86_64
conan install ~/workspace/gstreamer/conanfile.py --install-folder=build
conan build ~/workspace/gstreamer/conanfile.py --build-folder=build
rm -rf build
conan export-pkg --force ~/workspace/gstreamer/conanfile.py gstreamer/1.0@user/testing
conan remote add --force artifactory-conan-local http://172.16.64.65:8081/artifactory/api/conan/conan-local
conan user -p admin123 -r artifactory-conan-local admin
conan upload --force gstreamer/1.0@user/testing -r artifactory-conan-local --all