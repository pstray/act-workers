"""Setup script for the python-act library module"""

from os import path

from setuptools import setup

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), "rb") as f:
    long_description = f.read().decode("utf-8")

setup(
    name="act-workers",
    version="2.0.15",
    author="mnemonic AS",
    zip_safe=True,
    author_email="opensource@mnemonic.no",
    description="ACT workers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    keywords="ACT, mnemonic",
    entry_points={
        "console_scripts": [
            "act-argus-case = act.workers.argus_case:main_log_error",
            "act-attack = act.workers.attack:main_log_error",
            "act-country-regions = act.workers.country_regions:main_log_error",
            "act-fact-chain-helper = act.workers.fact_chain_helper:main_log_error",
            "act-feed = act.workers.act_feed:main_log_error",
            "act-hybrid-analysis-feed = act.workers.hybrid_analysis_feed:main_log_error",
            "act-ip-asn-history = act.workers.ip_asn_history:main_log_error",
            "act-ip-filter= act.workers.ip_filter:main_log_error",
            "act-isight = act.workers.isight:main_log_error",
            "act-misp-feeds = act.workers.misp_feeds:main_log_error",
            "act-mnemonic-pdns = act.workers.mnemonic_pdns:main_log_error",
            "act-scio = act.workers.scio:main_log_error",
            "act-search-graph = act.workers.search_graph:main_log_error",
            "act-shadowserver-asn = act.workers.shadowserver_asn:main_log_error",
            "act-shadowserver-enrich = act.workers.shadowserver_enrich:main_log_error",
            "act-ta-helper = act.workers.ta_helper:main_log_error",
            "act-thaicert = act.workers.thaicert:main_log_error",
            "act-tool-alias = act.workers.tool_alias:main_log_error",
            "act-uploader = act.workers.generic_uploader:main_log_error",
            "act-url-shorter-unpack = act.workers.url_shorter_unpack:main_log_error",
            "act-veris = act.workers.veris:main_log_error",
            "act-vt = act.workers.vt:main_log_error",
            "act-worker-config = act.workers.worker_config:main",
        ]
    },
    # Include ini-file(s) from act/workers/etc
    package_data={"act.workers": ["etc/*.ini"]},
    packages=["act.workers", "act.workers.libs"],
    # https://packaging.python.org/guides/packaging-namespace-packages/#pkgutil-style-namespace-packages
    # __init__.py under all packages under in the act namespace must contain exactly string:
    # __path__ = __import__('pkgutil').extend_path(__path__, __name__)
    namespace_packages=["act"],
    url="https://github.com/mnemonic-no/act-workers",
    install_requires=[
        "act-api>=2.0.5,<3.0.0",
        "act-types>=2.0.2,<3.0.0",
        "caep",
        "pid",
        "requests",
        "RashlyOutlaid>=0.19",
        "virustotal-api",
        "dateparser",
        "pyattck>=5.2.0",
    ],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: ISC License (ISCL)",
    ],
)
