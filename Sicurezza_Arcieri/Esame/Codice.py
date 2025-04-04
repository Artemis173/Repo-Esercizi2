import re
import os
import pandas as pd
import matplotlib.pyplot as plt

def parse_log_line(line):
    """
    Funzione per analizzare una riga del log, estraendo i dettagli come host, data, ora,
    metodo HTTP, pagina, status e byte trasferiti.
    """
    match = re.match(r'(\S+) - - \[(\d+/\w+/\d+):(\d+):\d+:\d+ .*\] "(\S+) (\S+) \S+" (\d+) (\d+)', line)
    if match:
        return match.groups()  # (host, date, hour, method, page, status, bytes)
    return None

def analyze_log(file_path, output_dir):
    """
    Funzione principale per analizzare il log e generare report dettagliati.
    Per ogni giorno del log, vengono effettuate diverse analisi:
    - Traffico giornaliero
    - Pagine più richieste
    - Errori (status >= 400)
    - Richieste per ora
    - Tipi di richieste HTTP
    - Codici di risposta
    - Host attivi
    - File più richiesti
    - Fascia oraria e data con più richieste
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    data = []
    with open(file_path, 'r', encoding='latin1') as file:
        for line in file:
            parsed = parse_log_line(line)
            if parsed:
                data.append(parsed)
    
    df = pd.DataFrame(data, columns=['host', 'date', 'hour', 'method', 'page', 'status', 'bytes'])
    df['status'] = df['status'].astype(int)
    df['bytes'] = df['bytes'].apply(lambda x: int(x) if x.isdigit() else 0)
    
    daily_traffic = {}
    for date, group in df.groupby('date'):
        total_requests = len(group)
        total_bytes = group['bytes'].sum() / (1024 * 1024)
        daily_traffic[date] = total_bytes

        # Analisi delle pagine più richieste
        page_counts = group['page'].value_counts().head(50)
        
        # Analisi degli errori (status >= 400)
        errors = group[group['status'] >= 400]
        error_count = len(errors)
        error_percentage = (error_count / total_requests) * 100 if total_requests else 0
        
        # Analisi degli host più attivi
        host_counts = group['host'].value_counts().head(50)
        
        # Analisi delle richieste per ora
        hourly_data = group.groupby('hour').agg({'host': 'count', 'bytes': lambda x: x.sum() / (1024 * 1024)})
        hourly_data.columns = ['Requests', 'MB Transferred']
        
        # Analisi dei tipi di richieste (GET, POST, PUT, etc.)
        request_types = group['method'].value_counts()
        
        # Analisi dei codici di risposta HTTP
        response_codes = group['status'].value_counts()
        
        # Analisi dei file più richiesti (per estensione)
        file_types = group['page'].str.extract(r'\.([a-zA-Z0-9]+)$')[0].value_counts()

        # Nuove analisi: gli host più e meno attivi, la fascia oraria con più richieste e la data con più richieste
        top_hosts = group['host'].value_counts().head(5)
        top_pages = group['page'].value_counts().head(5)
        busiest_hour = group.groupby('hour').size().idxmax()
        busiest_day = group.groupby('date').size().idxmax()

        # Contenuto del report
        report_lines = [
            f"Date: {date}",
            f"Total Requests: {total_requests}",
            f"Total MB Transferred: {total_bytes:.2f} MB",
            "\nRequests per Hour:",
            hourly_data.to_string(),
            "\nRequest Types:",
            request_types.to_string(),
            "\nResponse Codes:",
            response_codes.to_string(),
            f"\nTotal Errors: {error_count}",
            f"Error Percentage: {error_percentage:.2f}%",
            "\nFile Types Accessed:",
            file_types.to_string(),
            "\nTop 50 Pages Accessed:",
            page_counts.to_string(),
            "\nTop 50 Hosts Accessing:",
            host_counts.to_string(),
            "\nTop 5 Hosts Accessing:",
            top_hosts.to_string(),
            "\nTop 5 Pages Accessed:",
            top_pages.to_string(),
            f"Busiest Hour: {busiest_hour}",
            f"Busiest Day: {busiest_day}",
            "\n\n### Funzione 'Requests per Hour': Mostra come sono distribuite le richieste durante le varie ore del giorno.",
            "### Funzione 'Request Types': Mostra la distribuzione dei metodi HTTP (GET, POST, PUT, ecc.) per il giorno.",
            "### Funzione 'Response Codes': Mostra la distribuzione dei codici di risposta HTTP (200, 404, 500, ecc.) per il giorno.",
            "### Funzione 'Error Percentage': Calcola e mostra la percentuale di richieste con errori (status >= 400).",
            "### Funzione 'Top Pages Accessed': Mostra le 50 pagine più richieste nel giorno specificato.",
            "### Funzione 'Top Hosts Accessing': Mostra gli 50 host con il numero maggiore di richieste nel giorno.",
            "### Funzione 'Top Hosts and Pages': Mostra gli host e le pagine più visitate per identificare tendenze di traffico."
        ]
        
        report_content = "\n".join(report_lines)
        
        safe_date = date.replace("/", "-")
        report_filename = os.path.join(output_dir, f'report_{safe_date}.txt')
        with open(report_filename, 'w', encoding='utf-8') as out_file:
            out_file.write(report_content)
    
    # Report mensile
    total_requests_month = len(df)
    total_bytes_month = df['bytes'].sum() / (1024 * 1024)
    total_errors_month = len(df[df['status'] >= 400])
    total_success_month = total_requests_month - total_errors_month
    top_hosts = df['host'].value_counts().head(15)
    top_pages = df['page'].value_counts().head(15)
    hourly_data_month = df.groupby('hour').agg({'host': 'count', 'bytes': lambda x: x.sum() / (1024 * 1024)})
    hourly_data_month.columns = ['Requests', 'MB Transferred']
    request_types_month = df['method'].value_counts()
    response_codes_month = df['status'].value_counts()
    file_types_month = df['page'].str.extract(r'\.([a-zA-Z0-9]+)$')[0].value_counts()

    # Contenuto del report mensile
    summary_report_lines = [
        "Monthly Summary Report:",
        f"Total Requests: {total_requests_month}",
        f"Total MB Transferred: {total_bytes_month:.2f} MB",
    
        # Descrizione e dati per le richieste orarie
        "### Funzione 'Requests per Hour': Mostra la distribuzione delle richieste orarie per il mese.",
        "\nRequests per Hour:",
        hourly_data_month.to_string(),

        # Descrizione e dati per i tipi di richiesta
        "### Funzione 'Request Types': Mostra la distribuzione dei metodi HTTP (GET, POST, PUT, ecc.) per il mese.",
        "\nRequest Types:",
        request_types_month.to_string(),

        # Descrizione e dati per i codici di risposta
        "### Funzione 'Response Codes': Mostra la distribuzione dei codici di risposta HTTP (200, 404, 500, ecc.) per il mese.",
        "\nResponse Codes:",
        response_codes_month.to_string(),

        f"\nTotal Errors: {total_errors_month}",
        f"Error Percentage: {(total_errors_month / total_requests_month) * 100:.2f}%",
        
        # Descrizione e dati per i tipi di file
        "### Funzione 'File Types Accessed': Mostra la distribuzione dei tipi di file richiesti nel mese.",
        "\nFile Types Accessed:",
        file_types_month.to_string(),

        # Descrizione e dati per le pagine più visitate
        "### Funzione 'Top Pages Accessed': Mostra le 15 pagine più richieste nel mese.",
        "\nTop 15 Most Visited Pages:",
        top_pages.to_string(),

        # Descrizione e dati per gli host più attivi
        "### Funzione 'Top Hosts Accessing': Mostra i 15 host più attivi nel mese.",
        "\nTop 15 Most Active Hosts:",
        top_hosts.to_string()
    ]

    
    summary_report_content = "\n".join(summary_report_lines)
    
    summary_filename = os.path.join(output_dir, 'monthly_summary.txt')
    with open(summary_filename, 'w', encoding='utf-8') as summary_file:
        summary_file.write(summary_report_content)

    # Creazione dei grafici
    plt.figure(figsize=(10, 6))
    plt.bar(daily_traffic.keys(), daily_traffic.values(), color='blue')
    plt.xlabel('Date')
    plt.ylabel('MB Transferred')
    plt.title('Daily Network Traffic')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'daily_traffic.png'))
    plt.close()
    
    plt.figure(figsize=(8, 8))
    plt.pie(request_types_month, labels=request_types_month.index, autopct='%1.1f%%', startangle=140, shadow=True, explode=[0.1]*len(request_types_month))
    plt.title('Monthly Request Types Distribution')
    plt.savefig(os.path.join(output_dir, 'monthly_request_types.png'))
    plt.close()
    
    plt.figure(figsize=(8, 8))
    plt.pie(response_codes_month, labels=response_codes_month.index, autopct='%1.1f%%', startangle=140, shadow=True, explode=[0.1]*len(response_codes_month))
    plt.title('Monthly Response Codes Distribution')
    plt.savefig(os.path.join(output_dir, 'monthly_response_codes.png'))
    plt.close()

if __name__ == "__main__":
    analyze_log("NASA_access_log_Aug95.txt", "log_reports")






    #aggiorna
