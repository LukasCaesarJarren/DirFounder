import argparse
import os
from pptx import Presentation

class DirFounder:
    def __init__(self, semester, module, type_of_project, spec_dirs_l=None, spec_dirs_i=None):
        self.semester = semester
        self.module = module
        self.type_of_project = type_of_project
        self.spec_dirs_l = spec_dirs_l
        self.spec_dirs_i = spec_dirs_i
        self.base_folders_lecture = ["organizational", "scripts", "exercises"]
        self.base_dir = "/home/lukas/Documents/MSc_chemistry/semesters"
        self.base_folders_internship = ["organizational",
                                        "protocol/graphics",
                                        "presentations/short_presis",
                                        "presentations/main_pres",
                                        "literature"
                                        ]

    def create_lecture_dir_structure(self):
        if self.spec_dirs_l is not None:
            spec_dirs = self.spec_dirs_l.split(",")
            folders_to_create = self.base_folders_lecture + spec_dirs
        else:
            folders_to_create = self.base_folders_lecture

        for folder in folders_to_create:
            target_path = os.path.join(self.base_dir, self.semester, self.module, folder)
            os.makedirs(target_path)

    def create_internship_dir_structure(self):
        with open("/home/lukas/python_scripts_for_shell/new_study_project/tex_template.txt", "r") as file:
            tex_template = file.read()

        if self.spec_dirs_i is not None:
            spec_dirs = self.spec_dirs_i.split(",")
            folders_to_create = self.base_folders_internship + spec_dirs
        else:
            folders_to_create = self.base_folders_internship

        for folder in folders_to_create:
            if self.type_of_project == "LI" or self.type_of_project == "IL":
                target_path = os.path.join(self.base_dir, self.semester, self.module, "internship", folder)
                os.makedirs(target_path)
                if "protocol" in folder:
                    with open(
                            f"{self.base_dir}/{self.semester}/{self.module}/internship/protocol/Jarren_{self.module}_protocol_V1.tex",
                            "w") as file:
                        file.write(tex_template)
                if "main_pres" in folder:
                    prs = Presentation('/home/lukas/python_scripts_for_shell/new_study_project/pptx_template.pptx')
                    prs.save(f"{self.base_dir}/{self.semester}/{self.module}/internship/presentations/main_pres/Jarren_{self.module}_presentation_V1.pptx")
            else:
                target_path = os.path.join(self.base_dir, self.semester, self.module, folder)
                os.makedirs(target_path)
                if "protocol" in folder:
                    with open(
                            f"{self.base_dir}/{self.semester}/{self.module}/protocol/Jarren_{self.module}_protocol_V1.tex",
                            "w") as file:
                        file.write(tex_template)
                if "main_pres" in folder:
                    prs = Presentation('/home/lukas/python_scripts_for_shell/new_study_project/pptx_template.pptx')
                    prs.save(f"{self.base_dir}/{self.semester}/{self.module}/presentations/main_pres/Jarren_{self.module}_presentation_V1.pptx")

    def main(self):
        if self.type_of_project == "L":
            self.create_lecture_dir_structure()
        elif self.type_of_project == "I":
            self.create_internship_dir_structure()
        elif self.type_of_project == "LI" or self.type_of_project == "IL":
            self.create_lecture_dir_structure()
            self.create_internship_dir_structure()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-sem", type=str)
    parser.add_argument("-mod", type=str)
    parser.add_argument("-top", type=str)
    parser.add_argument("-sdirsl", type=str)
    parser.add_argument("-sdirsi", type=str)
    args = parser.parse_args()

    Founder = DirFounder(semester=args.sem,
                         module=args.mod,
                         type_of_project=args.top,
                         spec_dirs_l=args.sdirsl,
                         spec_dirs_i=args.sdirsi)

    Founder.main()
