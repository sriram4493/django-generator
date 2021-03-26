import click
from django.core.management.base import BaseCommand
import os
from generator import generate

# code_dir_path = os.path.dirname(os.path.realpath(__file__))
DEFAULT_OUTPUT_DIR = "core_app/core"
DEFAULT_MODULE = "core_app.core"

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("specification_path", type=str)
        parser.add_argument("--spec-format", type=str)
        parser.add_argument("--backend", type=str,
                      default="django")
        parser.add_argument("--verbose", default=False)
        parser.add_argument("--output-dir", type=str, default=DEFAULT_OUTPUT_DIR)
        parser.add_argument("--module-name", type=str, default=DEFAULT_MODULE,
                      help="The name of the module where the generated code will be "
                           "used, e.g. myproject.some_application")
        parser.add_argument("--urls-file", type=str, default="urls.py",
                      help="Use an alternative filename for the urls.")
        parser.add_argument("--views-file", type=str, default="views.py",
                      help="Use an alternative filename for the views.")
        parser.add_argument("--schemas-file", type=str, default="schemas.py",
                      help="Use an alternative filename for the schemas.")
        parser.add_argument("--utils-file", type=str, default="utils.py",
                      help="Use an alternative filename for the utilities.")
        parser.add_argument("--stubs-file", type=str, default="stubs.py",
                      help="Use an alternative filename for the utilities.")

    def handle(self, *args,**options):
        click.secho("Loading specification file......", fg="green")
        generate(options['specification_path'],options['spec_format'], options['backend'], options['verbose'],
             options['output_dir'], options['module_name'],options['urls_file'], options['views_file'],
             options['schemas_file'], options['utils_file'], options['stubs_file'])