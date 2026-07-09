print("=" * 21)
print(" FINANCIAL DASHBOARD ")
print("=" * 21,"\n")
print("Welcome! Please Begin:","\n")

assets = []
asset_count=0

total_assets = sum(assets)

#ENTER ASSETS
choice = "y"
# choice = "n"
while choice == "y":
    amount = float(input("Enter asset: "))
    assets.append(amount)
    asset_count += 1
    choice = input ("Add another? y/n ")

print(" ")

total_assets = sum(assets)

print(" ")

print("="*14)
print(" ASSET REPORT ")
print("="*14,"\n")


choice = print(assets,"\n")

for i in range(len(assets)):
    print(i + 1, "-", assets[i])
print(" ")

print("Assets Entered:",asset_count,"\n")

print(f"{'Total Assets':<20}${total_assets:>10,.2f}","\n")