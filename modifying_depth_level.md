# Modifying depth level

We use a custom sphinx **EnvironmentCollector** to make the **toctree** more interactible.
For that reason we also implemented our own way of changing the depth level of the **toctree**.

In order to change the **toctree** depth level locate the *conf.py* file and change / add the *depth* variable. For now only `depth=2` and `depth=3` make sense, since by default the toctree extends to 2 level and does not exceed 3.
