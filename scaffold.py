import os
import logging
#cookiecutter

class ProjectScaffold(object):
    def __init__(self, *args, **kw):
        pass

    def create_item(self):
        pass


class File(ProjectScaffold):
    def __init__(self, *args, **kw):
        ProjectScaffold.__init__(self, *args, **kw)
        self.name = args[0]
        self.content = args[1]

    def create_item(self):
        with open(self.name, 'w') as f:
            f.write(self.content)


class Directory(ProjectScaffold):
    def __init__(self, *args, **kw):
        ProjectScaffold.__init__(self, *args, **kw)
        self.name = args[0]
        self.children = []

    def add_item(self, child):
        self.children.append(child)

    def remove_item(self, child):
        self.children.remove(child)

    def create_item(self):
        os.mkdir(self.name)
        os.chdir(self.name)

        map(lambda x: x.create_item(), self.children)


class ProjectScaffoldClient(object):
    #def __init__(self, *args, **kw):
    #    pass

    def create_project(prj_name, prj_root):
        d0 = Directory(prj_name)




if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    logger.info('Start of Scaffolding ... ')

    d0 = Directory('')

    d1 = Directory('src')
    f1d1 = File('__init__.py',  '')
    d1.add_item(f1d1)
    d1.create_item()

    d2 = Directory('src/features')
    f1d2 = File('make_dataset.py')
    d2.add_item(f1d2)
    d2.create_item()

    logger.info('End of Scaffolding ... ')
