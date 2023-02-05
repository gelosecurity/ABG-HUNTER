# ABG-HUNTER
Automated Bug Gathering Hunter

![image](https://user-images.githubusercontent.com/49821326/216806882-36ee7192-c64e-4328-b07f-f303e76caf76.png)

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