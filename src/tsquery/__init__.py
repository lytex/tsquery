import logging
logger = logging.getLogger(__name__)

# TODO:
#  * Implement `tsview` which presents the available patterns (and their fields, if any) for the given language (should probably use Node and not Python)
#  * Implement `tsbuild` which builds .so from C source (using Python API `Language.build`)
#  * Refactor cli.py so that both tsbuild and tsquery are supported
