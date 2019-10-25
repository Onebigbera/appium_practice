# -*-coding:utf-8 -*-
# File :yaml_handler.py
# Author:George
# Date : 2019/10/24
# motto: Someone always give up while someone always try!
"""
    yaml data handler
"""
import yaml
import os


def yaml_data_handler(file_path):
    """

    :param file_path:
    :return:
    """
    with open(file_path, 'r') as f:
        data = yaml.load(f)
        print(data)
        print(type(data))
        print(data['name'])
        print(data['children'][1]['age'])
        data['name'] = 'george'
        print(data['name'])


def conversion_yaml():
    """
    convert python object to yaml data and write to file
    :return:
    """
    data ={
        'name': 'george',
        'age': 16,
        'friends':
        [{'name': 'marry', 'age': 16}, {'name': 'jack', 'age': 17}]
    }
    yaml_data = yaml.dump(data)
    dirname = os.path.dirname(os.path.dirname(__file__))
    # data_dir = os.path.join(dirname, 'data')
    data_dir = '/'.join([dirname, 'data'])
    file_path = data_dir + '/' + 'test.yaml'
    with open(file_path, 'w') as fw:
        fw.write(yaml_data)
    print(yaml_data)


if __name__ == "__main__":
    dirname = os.path.dirname(os.path.dirname(__file__))
    # data_dir = os.path.join(dirname, 'data')
    data_dir = '/'.join([dirname,  'data'])
    file_path = data_dir + '/' + 'familyInfo.yaml'
    print(data_dir)
    print(dirname)
    # file_path = r'F:\Appium\Projects\appium_practice\appium\data\familyInfo.yaml'
    yaml_data_handler(file_path)
    conversion_yaml()
