#!/usr/bin/env python3

from ansible import errors


def removekeys(dictionary, keys_to_remove):
    if isinstance(keys_to_remove, str):
        keys_to_remove = [keys_to_remove]

    if not isinstance(keys_to_remove, list):
        raise errors.AnsibleFilterError('keys to remove should be a list')

    if not isinstance(dictionary, dict):
        raise errors.AnsibleFilterError('removekeys expects a dict as input')

    new_dict = {}
    for k, v in dictionary.items():
        if k not in keys_to_remove:
            new_dict[k] = v

    return new_dict


class FilterModule(object):
    def filters(self):
        return {
            'removekeys': removekeys,
        }
