# ABG-HUNTER
### Automated Bug Gathering Hunter


This tool automates the process of bug bounty recon and vulnerability scanning. It requires all the tools to be in the user's local bin path.

![image](https://user-images.githubusercontent.com/49821326/216806935-c625bcaa-a895-44bc-b17a-6af910d6af93.png)

## Usage
`python3 ABG-Hunter.py -d <domain> [-e <exclude_file>]`

### Arguments

- `-d, --domain`: The target domain (required)
- `-e, --exclude-list`: File containing out of scope domains

## Tools Used

- Amass
- Subfinder
- Aquatone
- Httpx
- Naabu
- Nuclei

## Output

The output of the tool is saved in the following directories:

- `subdomains`: contains the combined and uniqued subdomains of the target domain
- `aquatone`: contains the output of Aquatone
- `httpx`: contains the output of Httpx
- `naabu`: contains the output of Naabu
- `nuclei`: contains the output of Nuclei
