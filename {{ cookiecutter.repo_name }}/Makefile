generate_root_key:
	cd ca && \
		openssl ecparam -name secp384r1 -genkey | openssl ec -aes-256-cbc -out root/private/root.key.pem && \
		chmod 0400 root/private/root.key.pem

generate_self_signed_root_cert:
	cd ca && \
		openssl req -config openssl.cnf -key root/private/root.key.pem -new -extensions ext_root -out root/certs/root.cert.pem -x509 -subj '/C={{ cookiecutter.country_code }}/ST={{ cookiecutter.state }}/O={{ cookiecutter.organization }}/OU={{ cookiecutter.organizational_unit }}/CN={{ cookiecutter.root_common_name }}' -days {{ cookiecutter.root_certificate_validity_in_days }}

generate_intermediate_key:
	cd ca && \
		openssl ecparam -name secp384r1 -genkey | openssl ec -aes-256-cbc -out intermediate/private/intermediate.key.pem && \
		chmod 400 intermediate/private/intermediate.key.pem

generate_intermediate_csr:
	cd ca && \
		openssl req -config openssl.cnf -new -key intermediate/private/intermediate.key.pem -out intermediate/csr/intermediate.csr.pem -subj '/C={{ cookiecutter.country_code }}/ST={{ cookiecutter.state }}/O={{ cookiecutter.organization }}/OU={{ cookiecutter.organizational_unit }}/CN={{ cookiecutter.intermediate_common_name }}'

sign_intermediate_csr_as_root:
	cd ca && \
		openssl ca -config openssl.cnf -name ca_root -extensions ext_intermediate -notext -in intermediate/csr/intermediate.csr.pem -out intermediate/certs/intermediate.cert.pem && \
		chmod 444 intermediate/certs/intermediate.cert.pem
