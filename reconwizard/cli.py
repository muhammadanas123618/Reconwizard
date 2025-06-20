import click
from datetime import datetime
from . import whois_lookup, dns_enum, subdomain_enum, port_scanner, banner_grabber, logger, report_generator ,tech_detect

@click.command()
@click.argument('domain')
@click.option('--whois', is_flag=True, help='Run WHOIS lookup')
@click.option('--dns', is_flag=True, help='Perform DNS enumeration')
@click.option('--subdomains', is_flag=True, help='Enumerate subdomains')
@click.option('--scan', is_flag=True, help='Scan ports')
@click.option('--banner', is_flag=True, help='Grab service banners')
@click.option('--tech', is_flag=True, help='Detect technologies using WhatWeb')
@click.option('--verbose', is_flag=True, help='Enable verbose logging')
def main(domain, whois, dns, subdomains, scan, banner, tech, verbose):
    log = logger.setup_logger()
    if verbose:
        log.setLevel('DEBUG')

    report_txt = f"Recon Report for {domain}\nGenerated: {datetime.now()}\n\n"
    html_data = {
        'domain': domain,
        'generated': datetime.now(),
        'whois': None,
        'dns_records': None,
        'subdomains': None,
        'open_ports': None,
        'technologies': None,
        'banners': None
    }

    if whois:
        log.info("Running WHOIS lookup")
        result = whois_lookup.run(domain)
        report_txt += f"\n--- WHOIS ---\n{result}\n"
        html_data['whois'] = result

    if dns:
        log.info("Running DNS enumeration")
        records = dns_enum.run(domain)
        for rtype, values in records.items():
            report_txt += f"{rtype}: {', '.join(values)}\n"
        html_data['dns_records'] = records

    if subdomains:
        log.info("Enumerating subdomains")
        subs = subdomain_enum.run(domain)
        report_txt += f"\n--- Subdomains ---\n" + "\n".join(subs) + "\n"
        html_data['subdomains'] = subs

    ports = []
    if scan:
        log.info("Scanning ports")
        ports = port_scanner.run(domain)
        report_txt += f"\n--- Open Ports ---\n" + ", ".join(map(str, ports)) + "\n"
        html_data['open_ports'] = ports

    if banner and ports:
        log.info("Grabbing banners")
        banners = banner_grabber.run(domain, ports)
        for port, b in banners.items():
            report_txt += f"Port {port}: {b}\n"
        html_data['banners'] = banners
        
    if tech:
       log.info("Detecting technologies")
       tech_result = tech_detect.run(domain)
       report_txt += f"\n--- Technologies ---\n{tech_result}\n"
       html_data['technologies'] = tech_result


    txt_path = f"reports/report_{domain}.txt"
    html_path = f"reports/report_{domain}.html"
    with open(txt_path, 'w') as f:
        f.write(report_txt)
    report_generator.generate_html_report(html_data, html_path)

    log.info(f"Reports saved to {txt_path} and {html_path}")
