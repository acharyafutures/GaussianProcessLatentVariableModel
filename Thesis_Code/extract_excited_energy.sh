#!/bin/bash
cat benzene_0000.log | grep "Lowest Energy" | tail -n1 | cut -d' ' -f20

