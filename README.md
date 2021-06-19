# iriscode

A portable OSIRIS V4.1, works on unix-like systems.

We first compile it in a docker and then copy those dependencies.

- remember to link those libs, see ``LD.sh``
- we correct the word case, i.e. ``CASIA-iRISv2`` => ``CASIA-IrisV2``
- we use dos2unix to remove \r in ``process.ini`` and ``process_CASIA-IrisV2.txt``


## Usage

```
export LD_LIBRARY_PATH=./lib:$LD_LIBRARY_PATH
./osiris ./data
```


## Acknowledge

[Authors of OSIRIS](http://svnext.it-sudparis.eu/svnview2-eph/ref_syst/Iris_Osiris_v4.1/download/Iris_Osiris_v4.1.tar.gz) (I can not open this link on June 19th 2021)

[5455945](https://github.com/5455945/Iris_Osiris)

[tohki](https://github.com/tohki/iris-osiris)
