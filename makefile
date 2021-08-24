#
#    Google Authenticator Export Helper.
#
#    2021-∞ (c) blurryroots innovation qanat OÜ. All rights reserved.
#    See license.md for details.
#
#    https://think-biq.com

FILE_PATH := $(abspath $(lastword $(MAKEFILE_LIST)))
PROJECT_DIR := $(shell dirname $(FILE_PATH))
PROJECT_NAME := $(notdir $(patsubst %/,%,$(dir $(FILE_PATH))))

DEBUG_FLAG :=
BUILD_PATH = "${PROJECT_DIR}/build"

ifeq '$(findstring ;,$(PATH))' ';'
	OS = "win"
	VENV_BIN_DIR = Scripts
	STD_FLAG = "/std:c++17 /EHa"
	EXE_NAME = gaeh
	BUILD_PATH_RELEASE = "${BUILD_PATH}/Release"
	EXE_PATH_RELEASE = "${BUILD_PATH_RELEASE}/${EXE_NAME}"
	BUILD_PATH_DEBUG = "${BUILD_PATH}/Debug"
	EXE_PATH_DEBUG = "${BUILD_PATH_DEBUG}/${EXE_NAME}"
	LLDB = lldb
	PYTHON = python
	PYTHON_EXECUTABLE := "${shell $(PYTHON) -c "import sys; print(sys.executable)"}"
else
	OS = "unix-y"
	VENV_BIN_DIR = bin
	STD_FLAG = "--std=c++17"
	EXE_NAME = gaeh
	BUILD_PATH_RELEASE = "${BUILD_PATH}"
	EXE_PATH_RELEASE = "${BUILD_PATH_RELEASE}/${EXE_NAME}"
	BUILD_PATH_DEBUG = "${BUILD_PATH}"
	EXE_PATH_DEBUG = "${BUILD_PATH_DEBUG}/${EXE_NAME}"
	LLDB = lldb
	PYTHON := python3
	PYTHON_EXECUTABLE := $(shell which $(PYTHON))
endif

CMD_ACTIVATE_VENV = . "$(PROJECT_DIR)/$(VENV_BIN_DIR)/activate"
CMD_DEACTIVATE_VENV = declare -f deactivate > /dev/null && deactivate

all: prepare build-wheel install-wheel

clean:
	$(CMD_DEACTIVATE_VENV)
	rm -rf pyvenv.cfg build dist

prepare:
	$(CMD_DEACTIVATE_VENV)
	python3 -m venv .
	$(CMD_ACTIVATE_VENV); pip install -r requirements.txt

build-wheel:
	$(CMD_ACTIVATE_VENV); python3 setup.py bdist_wheel

install-wheel: build-wheel
	$(CMD_ACTIVATE_VENV); python3 -m pip install gaeh \
		--force-reinstall --no-index --find-links="$(PROJECT_DIR)/dist"

venv-session:
	$(CMD_ACTIVATE_VENV); python3