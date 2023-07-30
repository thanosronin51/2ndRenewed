# Generated by Django 4.2.1 on 2023-07-15 04:09

from decimal import Decimal
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Withdrawal_internationa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.CharField(max_length=200)),
                ('recipient_bank_name', models.CharField(default='', max_length=200)),
                ('account_number', models.CharField(default='', max_length=200)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('10.00'))])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='pending', max_length=20)),
                ('date', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='withdrawals_international', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Manage Transfer_international',
                'verbose_name_plural': 'Manage Transfers_international',
            },
        ),
        migrations.CreateModel(
            name='Withdrawal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.CharField(max_length=200)),
                ('bank_sort_code', models.CharField(default='', max_length=200)),
                ('iban', models.CharField(default='', max_length=200)),
                ('swift_code', models.CharField(default='', max_length=200)),
                ('recipient_bank_name', models.CharField(choices=[('ABC International Bank Plc', 'ABC International Bank Plc'), ('Bank of America', 'Bank of America'), ('Citibank', 'Citibank'), ('JPMorgan Chase', 'JPMorgan Chase'), ('Wells Fargo', 'Wells Fargo'), ('Barclays', 'Barclays'), ('HSBC', 'HSBC'), ('Lloyds Banking Group', 'Lloyds Banking Group'), ('Royal Bank of Scotland', 'Royal Bank of Scotland'), ('Standard Chartered', 'Standard Chartered'), ('UBS', 'UBS'), ('Credit Suisse', 'Credit Suisse'), ('Deutsche Bank', 'Deutsche Bank'), ('Societe Generale', 'Societe Generale'), ('BNP Paribas', 'BNP Paribas'), ('ING Group', 'ING Group'), ('Rabobank', 'Rabobank'), ('Santander', 'Santander'), ('BBVA', 'BBVA'), ('CaixaBank', 'CaixaBank'), ('Itau Unibanco', 'Itau Unibanco'), ('Bradesco', 'Bradesco'), ('Bank of China', 'Bank of China'), ('Industrial and Commercial Bank of China', 'Industrial and Commercial Bank of China'), ('China Construction Bank', 'China Construction Bank'), ('Agricultural Bank of China', 'Agricultural Bank of China'), ('Bank of Communications', 'Bank of Communications'), ('Mitsubishi UFJ Financial Group', 'Mitsubishi UFJ Financial Group'), ('Sumitomo Mitsui Financial Group', 'Sumitomo Mitsui Financial Group'), ('Mizuho Financial Group', 'Mizuho Financial Group'), ('Nomura Holdings', 'Nomura Holdings'), ('Resona Holdings', 'Resona Holdings'), ('Sberbank', 'Sberbank'), ('VTB Bank', 'VTB Bank'), ('Gazprombank', 'Gazprombank'), ('Alfa-Bank', 'Alfa-Bank'), ('Promsvyazbank', 'Promsvyazbank'), ('Rosbank', 'Rosbank'), ('Korea Development Bank', 'Korea Development Bank'), ('KB Financial Group', 'KB Financial Group'), ('Shinhan Financial Group', 'Shinhan Financial Group'), ('Woori Financial Group', 'Woori Financial Group'), ('Hana Financial Group', 'Hana Financial Group'), ('NongHyup Financial Group', 'NongHyup Financial Group'), ('Bank Mandiri', 'Bank Mandiri'), ('Bank Central Asia', 'Bank Central Asia'), ('Bank Rakyat Indonesia', 'Bank Rakyat Indonesia'), ('Bank Negara Indonesia', 'Bank Negara Indonesia'), ('OCBC Bank', 'OCBC Bank'), ('DBS Bank', 'DBS Bank'), ('United Overseas Bank', 'United Overseas Bank'), ('Bangkok Bank', 'Bangkok Bank'), ('Siam Commercial Bank', 'Siam Commercial Bank'), ('Kasikornbank', 'Kasikornbank'), ('Krung Thai Bank', 'Krung Thai Bank'), ('TMB Bank', 'TMB Bank'), ('Standard Bank Group', 'Standard Bank Group'), ('FirstRand Bank', 'FirstRand Bank'), ('Nedbank', 'Nedbank'), ('Investec', 'Investec'), ('Capitec Bank', 'Capitec Bank'), ('Bank of Montreal', 'Bank of Montreal'), ('Toronto-Dominion Bank', 'Toronto-Dominion Bank'), ('Royal Bank of Canada', 'Royal Bank of Canada'), ('Scotiabank', 'Scotiabank'), ('National Australia Bank', 'National Australia Bank'), ('Australia and New Zealand Banking Group', 'Australia and New Zealand Banking Group'), ('Commonwealth Bank', 'Commonwealth Bank'), ('Westpac Banking Corporation', 'Westpac Banking Corporation'), ('National Bank of Australia', 'National Bank of Australia'), ('BNZ', 'BNZ'), ('ASB Bank', 'ASB Bank'), ('Kiwibank', 'Kiwibank'), ('Bank of New Zealand', 'Bank of New Zealand'), ('Banco Santander', 'Banco Santander'), ('BBVA', 'BBVA'), ('CaixaBank', 'CaixaBank'), ('Bankia', 'Bankia'), ('Banco Sabadell', 'Banco Sabadell'), ('ING Group', 'ING Group'), ('ABN AMRO', 'ABN AMRO'), ('Rabobank', 'Rabobank'), ('SNS Bank', 'SNS Bank'), ('Banco de Chile', 'Banco de Chile'), ('BancoEstado', 'BancoEstado'), ('Santander Chile', 'Santander Chile'), ('Banco de Crédito e Inversiones', 'Banco de Crédito e Inversiones'), ('Banco Santander (Mexico)', 'Banco Santander (Mexico)'), ('BBVA Bancomer', 'BBVA Bancomer'), ('Banorte', 'Banorte'), ('HSBC Mexico', 'HSBC Mexico'), ('Citigroup', 'Citigroup'), ('JPMorgan Chase', 'JPMorgan Chase'), ('Bank of America', 'Bank of America'), ('Wells Fargo', 'Wells Fargo'), ('TD Bank', 'TD Bank'), ('Scotiabank', 'Scotiabank'), ('Morgan Stanley', 'Morgan Stanley'), ('Goldman Sachs', 'Goldman Sachs'), ('BNY Mellon', 'BNY Mellon'), ('State Street Corporation', 'State Street Corporation'), ('Northern Trust', 'Northern Trust'), ('PNC Financial Services', 'PNC Financial Services'), ('Capital One', 'Capital One'), ('Fifth Third Bancorp', 'Fifth Third Bancorp'), ('SunTrust Banks', 'SunTrust Banks'), ('KeyCorp', 'KeyCorp'), ('American Express', 'American Express'), ('Discover Financial', 'Discover Financial'), ('BB&T Corporation', 'BB&T Corporation'), ('Regions Financial Corporation', 'Regions Financial Corporation'), ('Huntington Bancshares', 'Huntington Bancshares'), ('Ally Financial', 'Ally Financial'), ('First Republic Bank', 'First Republic Bank'), ('Synchrony Financial', 'Synchrony Financial'), ('USAA', 'USAA'), ('Comerica', 'Comerica'), ('Zions Bancorp', 'Zions Bancorp'), ('SVB Financial Group', 'SVB Financial Group'), ('E*TRADE', 'E*TRADE'), ('Ameriprise Financial', 'Ameriprise Financial'), ('Raymond James Financial', 'Raymond James Financial'), ('LPL Financial', 'LPL Financial'), ('Stifel Financial', 'Stifel Financial'), ('Janney Montgomery Scott', 'Janney Montgomery Scott'), ('Jefferies Financial Group', 'Jefferies Financial Group'), ('Robert W. Baird', 'Robert W. Baird'), ('Cowen Group', 'Cowen Group'), ('Evercore', 'Evercore'), ('Houlihan Lokey', 'Houlihan Lokey'), ('Moelis & Company', 'Moelis & Company'), ('Oppenheimer Holdings', 'Oppenheimer Holdings'), ('Piper Sandler', 'Piper Sandler'), ('RBC Capital Markets', 'RBC Capital Markets'), ('Stephens Inc.', 'Stephens Inc.'), ('SunTrust Robinson Humphrey', 'SunTrust Robinson Humphrey'), ('William Blair & Company', 'William Blair & Company'), ('M&T Bank', 'M&T Bank'), ('Associated Banc-Corp', 'Associated Banc-Corp'), ('TCF Financial Corporation', 'TCF Financial Corporation'), ('First Horizon National Corporation', 'First Horizon National Corporation'), ('Commerce Bancshares', 'Commerce Bancshares'), ('Popular, Inc.', 'Popular, Inc.'), ('BOK Financial Corporation', 'BOK Financial Corporation'), ('Synovus', 'Synovus'), ('Hancock Whitney Corporation', 'Hancock Whitney Corporation'), ('Cathay Bank', 'Cathay Bank'), ('East West Bank', 'East West Bank'), ('First Citizens BancShares', 'First Citizens BancShares'), ('Webster Financial Corporation', 'Webster Financial Corporation'), ('City National Bank', 'City National Bank'), ('Wintrust Financial Corporation', 'Wintrust Financial Corporation'), ('Texas Capital Bancshares', 'Texas Capital Bancshares'), ('Signature Bank', 'Signature Bank'), ('New York Community Bancorp', 'New York Community Bancorp'), ('F.N.B. Corporation', 'F.N.B. Corporation'), ('First Hawaiian Bank', 'First Hawaiian Bank'), ('Huntington Bancshares', 'Huntington Bancshares'), ('Bank of the West', 'Bank of the West'), ('CIT Group', 'CIT Group'), ('NBT Bancorp', 'NBT Bancorp'), ('PacWest Bancorp', 'PacWest Bancorp'), ('Western Alliance Bancorporation', 'Western Alliance Bancorporation'), ('Greenhill & Co.', 'Greenhill & Co.'), ('PJT Partners', 'PJT Partners'), ('Houlihan Lokey', 'Houlihan Lokey'), ('Moelis & Company', 'Moelis & Company'), ('Centerview Partners', 'Centerview Partners'), ('Qatalyst Partners', 'Qatalyst Partners'), ('Guggenheim Partners', 'Guggenheim Partners'), ('Moelis & Company', 'Moelis & Company'), ('Evercore', 'Evercore'), ('Rothschild & Co', 'Rothschild & Co'), ('Greenhill & Co.', 'Greenhill & Co.')], default='', max_length=200)),
                ('description', models.CharField(default='', max_length=80)),
                ('account_number', models.CharField(default='', max_length=200)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('10.00'))])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='pending', max_length=20)),
                ('date', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='withdrawals', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Manage Transfer',
                'verbose_name_plural': 'Manage Transfers',
            },
        ),
        migrations.CreateModel(
            name='SUPPORT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tickets', models.CharField(choices=[('Please Select Customer Service Department', 'Please Select Customer Service Department'), ('Request For Transaction Files', 'Request For Transaction Files'), ('Customer Services Department', 'Customer Services Department'), ('Account Department', 'Account Department'), ('Transfer Department', 'Transfer Department'), ('Card Services Department', 'Card Services Department'), ('Loan Department', 'Loan Department'), ('Bank Deposit Department', 'Bank Deposit Department')], max_length=255)),
                ('message', models.CharField(max_length=500)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'SUPPORT',
                'verbose_name_plural': 'SUPPORTs',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(choices=[('USDT_ERC20', 'USDT ERC20'), ('USDT_TRC20', 'USDT TRC20'), ('ETHEREUM', 'Ethereum'), ('BITCOIN', 'Bitcoin'), ('STELLAR', 'STELLAR'), ('RIPPLE', 'RIPPLE'), ('LITECOIN', 'LITECOIN')], max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('proof_of_pay', models.ImageField(blank=True, null=True, upload_to='proofs/')),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('COMPLETE', 'Complete')], default='PENDING', max_length=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Manage Deposit/Payment',
                'verbose_name_plural': 'Manage Deposit/Payment',
            },
        ),
        migrations.CreateModel(
            name='PayBills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(max_length=512)),
                ('address2', models.CharField(default='', max_length=512)),
                ('city', models.CharField(max_length=512)),
                ('state', models.CharField(max_length=512)),
                ('zipcode', models.CharField(max_length=512)),
                ('nickname', models.CharField(max_length=512)),
                ('delivery_method', models.CharField(choices=[('Paper Check', 'Paper Check'), ('Digital Receipt', 'Digital Receipt')], default='', max_length=200)),
                ('memo', models.CharField(default='', max_length=80)),
                ('account_number', models.CharField(default='', max_length=200)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('10.00'))])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('day', models.PositiveIntegerField()),
                ('month', models.PositiveIntegerField()),
                ('year', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='pending', max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pay_bills', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Manage Bills',
                'verbose_name_plural': 'Manage Bills',
            },
        ),
        migrations.CreateModel(
            name='LoanRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit_facility', models.CharField(choices=[('Personal Home Loans', 'Personal Home Loans'), ('Joint Mortgage', 'Joint Mortgage'), ('Automobile Loans', 'Automobile Loans'), ('Salary loans', 'Salary loans'), ('Secured Overdraft', 'Secured Overdraft'), ('Contract Finance', 'Contract Finance'), ('Secured Term Loans', 'Secured Term Loans'), ('StartUp/Products Financing', 'StartUp/Products Financing'), ('Local Purchase Orders Finance', 'Local Purchase Orders Finance'), ('Operational Vehicles', 'Operational Vehicles'), ('Revenue Loans and Overdraft', 'Revenue Loans and Overdraft'), ('Retail TOD', 'Retail TOD'), ('Commercial Mortgage', 'Commercial Mortgage'), ('Office Equipment', 'Office Equipment'), ('Health Finance Product Guideline', 'Health Finance Product Guideline'), ('Health Finance', 'Health Finance')], default='', max_length=40)),
                ('payment_tenure', models.CharField(choices=[('6 Months', '6 Months'), ('12 Months', '12 Months'), ('2 Years', '2 Years'), ('3 Years', '3 Years'), ('4 Years', '4 Years'), ('5 Years', '5 Years')], default='', max_length=40)),
                ('reason', models.TextField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('requested_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Diposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('10.00'))])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deposits', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CryptoWITHDRAW',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(choices=[('USDT_ERC20', 'USDT ERC20'), ('USDT_TRC20', 'USDT TRC20'), ('ETHEREUM', 'Ethereum'), ('BITCOIN', 'Bitcoin'), ('STELLAR', 'STELLAR'), ('RIPPLE', 'RIPPLE'), ('LITECOIN', 'LITECOIN')], max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('recipient_address', models.CharField(default='', max_length=512)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('COMPLETE', 'Complete')], default='PENDING', max_length=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Crypto Withdrawal',
                'verbose_name_plural': 'Crypto Withdrawals',
            },
        ),
        migrations.CreateModel(
            name='CHECK_DEPOSIT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('front_image', models.ImageField(blank=True, null=True, upload_to='deposits/')),
                ('back_image', models.ImageField(blank=True, null=True, upload_to='deposits/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Check Deposit',
                'verbose_name_plural': 'Check Deposits',
            },
        ),
        migrations.CreateModel(
            name='CardDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_type', models.CharField(choices=[('V', 'Visa'), ('M', 'Mastercard'), ('D', 'Discover'), ('A', 'American Express'), ('CUP', 'China Union Pay'), ('DC', 'Dollar Card'), ('MC', 'Master Card'), ('VC', 'Visa Card'), ('JC', 'JCB Card'), ('AE', 'American Express'), ('UB', 'Union Bank Card'), ('BC', 'Bank Card'), ('EB', 'Eurocard'), ('NC', 'Nordic Card'), ('AC', 'Asian Card'), ('IC', 'International Card'), ('MC', 'Maestro Card'), ('EC', 'Eurocheque Card'), ('GC', 'Global Card'), ('UC', 'Uba Card'), ('FC', 'First Bank Card'), ('ZC', 'Zenith Bank Card'), ('AC', 'Access Bank Card'), ('GC', 'GTBank Card'), ('KC', 'Keystone Bank Card'), ('EC', 'Ecobank Card'), ('IC', 'UBA International Card'), ('OC', 'Other Card')], max_length=255)),
                ('card_number', models.CharField(max_length=255)),
                ('expiry_month', models.PositiveIntegerField()),
                ('expiry_year', models.PositiveIntegerField()),
                ('cvv', models.CharField(max_length=3)),
                ('card_owner', models.CharField(blank=True, max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Card Detail',
                'verbose_name_plural': 'Card Details',
            },
        ),
    ]
