import argparse
import os

def pink_print(message):
    print(f'\033[95m{message}\033[0m')


pink_print('')
pink_print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
pink_print('█░▄▄▀██░▄▄▀██░▄▄░████░██░██░██░██░▀██░█▄▄░▄▄██░▄▄▄██░▄▄▀')
pink_print('█░▀▀░██░▄▄▀██░█▀▀████░▄▄░██░██░██░█░█░███░████░▄▄▄██░▀▀▄')
pink_print('█░██░██░▀▀░██░▀▀▄████░██░██▄▀▀▄██░██▄░███░████░▀▀▀██░██░')
pink_print('▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀')
pink_print('Automated Bug Gathering Hunter')

def parse_args():
    parser = argparse.ArgumentParser(description='Automate bug bounty recon and vulnerability scanning')
    parser.add_argument('-d', '--domain', dest='domain', required=True, help='The target domain')
    parser.add_argument('-e', '--exclude-list', dest='exclude_list', help='File containing out of scope domains')
    return parser.parse_args()

def run_command(command):
    os.system(command)

def get_exclude_list(exclude_file):
    exclude_list = []
    if exclude_file is not None:
        with open(exclude_file, 'r') as f:
            exclude_list = [line.strip() for line in f.readlines()]
    return exclude_list

def main():
    args = parse_args()
    domain = args.domain
    exclude_list = get_exclude_list(args.exclude_list)

    # Subdomain Enumeration
    os.makedirs('subdomains', exist_ok=True)
    pink_print('Running Amass...')
    run_command(f'amass enum -d {domain} > subdomains/amass_output.txt')
    pink_print('Running Subfinder...')
    run_command(f'subfinder -d {domain} > subdomains/subfinder_output.txt')

    # Combine and uniq the subdomains
    run_command(f"cat subdomains/amass_output.txt subdomains/subfinder_output.txt | sort -u > subdomains/all_subdomains.txt")

    # Filter out the excluded domains
    with open('subdomains/all_subdomains.txt', 'r') as f:
        all_subdomains = f.readlines()
    with open('subdomains/all_subdomains.txt', 'w') as f:
        for subdomain in all_subdomains:
            if not any(excluded in subdomain for excluded in exclude_list):
                f.write(subdomain)

    # Web
    os.makedirs('aquatone', exist_ok=True)
    pink_print('Running Aquatone...')
    run_command(f'cat subdomains/all_subdomains.txt | aquatone -out aquatone_report')

    os.makedirs('httpx', exist_ok=True)
    pink_print('Running Httpx...')
    run_command(f'cat subdomains/all_subdomains.txt | httpx -t 1 -o httpx/httpx_output.txt')

    # Network
    os.makedirs('naabu', exist_ok=True)
    pink_print('Running Naabu...')
    run_command(f'cat subdomains/all_subdomains.txt | naabu -o naabu/naabu_output.txt')

	  # Vuln Scanning
    os.makedirs('nuclei', exist_ok=True)
    pink_print('Running Nuclei...')

		# Changed rate limit to match bug bounty scope. Make sure you check your program's scope and limiting of requests!
    run_command(f'nuclei -t -l subdomains/all_subdomains.txt -o nuclei/nuclei_output.txt --rate-limit 500ms --rate-limit-host 1')

if __name__ == '__main__':
    main()
