#!/usr/bin/env python
import json
import os
import sys
import time


class Utils(object):

    @classmethod
    def debug_print(cls, message):
        """
        print a message to stderr.
        Concourse take everything printed in stdout as an output
        :param message: message to print
        :return:
        """
        sys.stderr.write(message + "\n")

    @classmethod
    def version_to_output(cls, input_version):
        """
        Convert single k/v version dict into `version`/`metadata` output.
        """
        output = {'version': {"ref": input_version["ref"]}}
        if len(input_version) > 1:
            update_dict = {'metadata': [
                {"name": k, "value": v} for k, v in input_version.items() if not k == "timestamp"
            ]
            }

            output.update(update_dict)
        return output


class FakeResource(object):

    def __init__(self, json_data, command_argument):
        Utils.debug_print("Concourse fake resource started")
        Utils.debug_print("json_data: %s" % json_data)
        Utils.debug_print("command_argument: %s" % command_argument)

        self.json_data = json_data
        self.command_argument = command_argument

    def run(self, command_name):
        Utils.debug_print("command_name: %s" % command_name)
        output = None
        if command_name == 'check':
            output = self.cmd_check()
            output = [output]
        if command_name == 'in':
            output = self.cmd_in()
        if command_name == 'out':
            output = self.cmd_out()

        return json.dumps(output)

    @staticmethod
    def cmd_check():

        # this will be the returned version object
        version = dict()
        version["ref"] = "fake"

        return version

    def cmd_in(self):
        version = self.json_data["version"]

        return Utils.version_to_output(version)

    def cmd_out(self):

        version = self.cmd_check()

        return Utils.version_to_output(version)


def main():
    mrepo_resource = FakeResource(json.load(sys.stdin), sys.argv[1:])
    print(mrepo_resource.run(os.path.basename(__file__)))


if __name__ == '__main__':
    main()
