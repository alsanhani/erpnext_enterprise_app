ARG FRAPPE_BRANCH=version-15
FROM frappe/erpnext:${FRAPPE_BRANCH}

USER root
RUN apt-get update && apt-get install -y --no-install-recommends git && rm -rf /var/lib/apt/lists/*

USER frappe
COPY --chown=frappe:frappe . /home/frappe/frappe-bench/apps/my_custom_app
RUN /home/frappe/frappe-bench/env/bin/pip install -e /home/frappe/frappe-bench/apps/my_custom_app
