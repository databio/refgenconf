""" Tests for listing remotely available genomes and assets. """

import mock
from refgenconf import RefGenConf, CFG_FOLDER_KEY, CFG_GENOMES_KEY, \
    CFG_SERVERS_KEY, DEFAULT_SERVER

__author__ = "Vince Reuter"
__email__ = "vreuter@virginia.edu"


def test_list_remote(rgc, tmpdir):
    """ Verify expected behavior of remote genome/asset listing. """
    new_rgc = RefGenConf(entries={CFG_FOLDER_KEY: tmpdir.strpath,
                          CFG_SERVERS_KEY: DEFAULT_SERVER,
                          CFG_GENOMES_KEY: rgc[CFG_GENOMES_KEY]})
    new_rgc[CFG_SERVERS_KEY] = "https://refgenomes.databio.org/"
    print("NEW RGC KEYS: {}".format(list(new_rgc.keys())))
    with mock.patch("refgenconf.refgenconf._read_remote_data",
                    return_value=rgc.genomes):
        genomes, assets = new_rgc.get_remote_data_str()
    _assert_eq_as_sets(rgc.genomes_str(), genomes)


def _assert_eq_as_sets(a, b):
    """ Collections are equivalent as sets if they're equal in size and element's collective identity. """
    assert len(a) == len(b)
    assert set(a) == set(b)
