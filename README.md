# ABG-HUNTER
### Automated Bug Gathering Hunter
![image](https://user-images.githubusercontent.com/49821326/216807044-c3de5c7d-da4f-4b01-8f50-b1c78366f3ec.png)

This tool automates the process of bug bounty recon and vulnerability scanning. It requires all the tools to be in the user's local bin path.

![image](https://user-images.githubusercontent.com/49821326/216807028-18e249f2-4c4e-4608-93b1-64a826ced93c.png)

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
