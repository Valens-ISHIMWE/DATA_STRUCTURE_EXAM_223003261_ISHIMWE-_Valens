#include <iostream>
#include <algorithm> // for sort
using namespace std;

// Denomination struct
struct Denomination {
    int value;
    int* count;
};

// Abstract base class
class Dispenser {
protected:
    Denomination* denoms;
    int size;
public:
    Dispenser(Denomination* d, int s) : denoms(d), size(s) {}
    virtual bool withdraw(int amount) = 0;
};

// Greedy Dispenser
class GreedyDispenser : public Dispenser {
public:
    GreedyDispenser(Denomination* d, int s) : Dispenser(d, s) {}

    bool withdraw(int amount) override {
        cout << "Using Greedy Strategy...\n";
        for (int i = 0; i < size; ++i) {
            while (*(denoms[i].count) > 0 && amount >= denoms[i].value) {
                amount -= denoms[i].value;
                (*(denoms[i].count))--;
                cout << "Dispensed: " << denoms[i].value << "\n";
            }
        }
        if (amount == 0) {
            cout << "Withdrawal Successful!\n";
            return true;
        } else {
            cout << "Cannot dispense full amount with available notes.\n";
            return false;
        }
    }
};

// Optimal Dispenser
class OptimalDispenser : public Dispenser {
public:
    OptimalDispenser(Denomination* d, int s) : Dispenser(d, s) {}

    bool withdraw(int amount) override {
        cout << "Using Optimal Strategy...\n";
        int* used = new int[size];
        for (int i = 0; i < size; ++i) used[i] = 0;

        int remaining = amount;
        for (int i = 0; i < size; ++i) {
            int take = min(remaining / denoms[i].value, *(denoms[i].count));
            used[i] = take;
            remaining -= take * denoms[i].value;
        }

        if (remaining == 0) {
            for (int i = 0; i < size; ++i)
                *(denoms[i].count) -= used[i];
            for (int i = 0; i < size; ++i)
                for (int j = 0; j < used[i]; ++j)
                    cout << "Dispensed: " << denoms[i].value << "\n";
            cout << "Withdrawal Successful!\n";
            delete[] used;
            return true;
        } else {
            cout << "Cannot dispense full amount optimally.\n";
            delete[] used;
            return false;
        }
    }
};

// Sort denominations from high to low
void sortDenoms(Denomination*& denoms, int size) {
    sort(denoms, denoms + size, [](Denomination a, Denomination b) {
        return a.value > b.value;
    });
}

// Add Denomination
void addDenomination(Denomination*& denoms, int& size, int value, int count) {
    for (int i = 0; i < size; ++i) {
        if (denoms[i].value == value) {
            *(denoms[i].count) += count;
            return;
        }
    }
    Denomination* newArr = new Denomination[size + 1];
    for (int i = 0; i < size; ++i) newArr[i] = denoms[i];
    newArr[size].value = value;
    newArr[size].count = new int(count);
    delete[] denoms;
    denoms = newArr;
    size++;
    sortDenoms(denoms, size);
}

// Remove Denomination
void removeDenomination(Denomination*& denoms, int& size, int value) {
    int index = -1;
    for (int i = 0; i < size; ++i)
        if (denoms[i].value == value)
            index = i;

    if (index == -1) {
        cout << "Denomination not found.\n";
        return;
    }

    delete denoms[index].count;
    Denomination* newArr = new Denomination[size - 1];
    for (int i = 0, j = 0; i < size; ++i)
        if (i != index)
            newArr[j++] = denoms[i];
    delete[] denoms;
    denoms = newArr;
    size--;
}

// Show Denominations
void showDenominations(Denomination* denoms, int size) {
    cout << "removed Denominations:\n";
    for (int i = 0; i < size; ++i)
        cout << denoms[i].value << " Rwf x " << *(denoms[i].count) << "\n";
}

void pauseAndContinue() {
    cout << "Press Enter to continue...";
    cin.ignore();
    cin.get();
}

int main() {
    Denomination* denoms = nullptr;
    int denomSize = 0;
    Dispenser* machines[2] = { nullptr, nullptr };

    int choice;
    do {
        cout << "\n=== ATM Cash Dispenser ===\n";
        cout << "1. Add Denomination\n";
        cout << "2. Remove Denomination\n";
        cout << "3. Show Denominations\n";
        cout << "4. Withdraw (Greedy)\n";
        cout << "5. Withdraw (Optimal)\n";
        cout << "0. Exit\n";
        cout << "Enter choice: ";
        cin >> choice;

        int value, count, amount;

        switch (choice) {
        case 1:
            cout << "Enter denomination value: ";
            cin >> value;
            cout << "Enter number of notes: ";
            cin >> count;
            addDenomination(denoms, denomSize, value, count);
            cin.ignore();
            pauseAndContinue();
            break;
        case 2:
            cout << "Enter denomination value to remove: ";
            cin >> value;
            removeDenomination(denoms, denomSize, value);
            cin.ignore();
            pauseAndContinue();
            break;
        case 3:
            showDenominations(denoms, denomSize);
            cin.ignore();
            pauseAndContinue();
            break;
        case 4:
            if (machines[0]) delete machines[0];
            machines[0] = new GreedyDispenser(denoms, denomSize);
            cout << "Enter amount to withdraw: ";
            cin >> amount;
            machines[0]->withdraw(amount);
            cin.ignore();
            pauseAndContinue();
            break;
        case 5:
            if (machines[1]) delete machines[1];
            machines[1] = new OptimalDispenser(denoms, denomSize);
            cout << "Enter amount to withdraw: ";
            cin >> amount;
            machines[1]->withdraw(amount);
            cin.ignore();
            pauseAndContinue();
            break;
        case 0:
            cout << "Exiting...\n";
            break;
        default:
            cout << "Invalid choice.\n";
            cin.ignore();
            pauseAndContinue();
        }
    } while (choice != 0);

    for (int i = 0; i < denomSize; ++i)
        delete denoms[i].count;
    delete[] denoms;

    for (int i = 0; i < 2; ++i)
        delete machines[i];

    return 0;
}

