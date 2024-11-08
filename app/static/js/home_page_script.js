window.onload = function() {
    const numFields = document.getElementById("numFields");
    const inputContainer = document.getElementById("inputContainer");
    const objectiveFunction = document.getElementById("objectiveFunction");
    const singleNumberField = document.getElementById("singleNumberField");
    const constraintsContainer = document.getElementById("constraintsContainer");

    function createObjectiveFunction(num) {
        objectiveFunction.innerHTML = "";

        const objectiveLabel = document.createElement("h3");
        objectiveLabel.innerText = "Função Objetivo:";
        objectiveFunction.appendChild(objectiveLabel);

        const zEquation = document.createElement("div");
        zEquation.classList.add("mt-2");

        const zText = document.createElement("span");
        zText.innerText = "Z = ";
        zEquation.appendChild(zText);

        for (let i = 0; i < num; i++) {
            const coefInput = document.createElement("input");
            coefInput.type = "number";
            coefInput.placeholder = `Coef ${i + 1}`;
            coefInput.classList.add("form-control", "d-inline", "mx-1", "coef-input");

            const varText = document.createElement("span");
            varText.innerHTML = `X${i + 1}`;
            zEquation.appendChild(coefInput);
            zEquation.appendChild(varText);

            if (i < num - 1) {
                const plusSign = document.createElement("span");
                plusSign.innerText = " + ";
                zEquation.appendChild(plusSign);
            }
        }

        objectiveFunction.appendChild(zEquation);
    }

    function createConstraints(numVariables, numConstraints) {
        constraintsContainer.innerHTML = "";

        if (numConstraints > 0) {
            const constraintsLabel = document.createElement("h3");
            constraintsLabel.innerText = "Restrições:";
            constraintsContainer.appendChild(constraintsLabel);

            for (let i = 0; i < numConstraints; i++) {
                const constraintRow = document.createElement("div");
                constraintRow.classList.add("mt-2", "d-flex", "align-items-center");

                for (let j = 0; j < numVariables; j++) {
                    const coefInput = document.createElement("input");
                    coefInput.type = "number";
                    coefInput.placeholder = `Coef ${j + 1}`;
                    coefInput.classList.add("form-control", "d-inline", "mx-1", "coef-input");

                    const varText = document.createElement("span");
                    varText.innerHTML = `X${j + 1}`;
                    constraintRow.appendChild(coefInput);
                    constraintRow.appendChild(varText);

                    if (j < numVariables - 1) {
                        const plusSign = document.createElement("span");
                        plusSign.innerText = " + ";
                        constraintRow.appendChild(plusSign);
                    }
                }

                const selectOperator = document.createElement("select");
                selectOperator.classList.add("form-select", "d-inline", "mx-1");

                const optionLeq = document.createElement("option");
                optionLeq.value = "<=";
                optionLeq.text = "≤";
                selectOperator.appendChild(optionLeq);

                const optionGeq = document.createElement("option");
                optionGeq.value = ">=";
                optionGeq.text = "≥";
                selectOperator.appendChild(optionGeq);

                constraintRow.appendChild(selectOperator);

                const resultInput = document.createElement("input");
                resultInput.type = "number";
                resultInput.placeholder = "Valor";
                resultInput.classList.add("form-control", "d-inline", "mx-1", "coef-input");
                constraintRow.appendChild(resultInput);

                constraintsContainer.appendChild(constraintRow);
            }
        } else {
            constraintsContainer.innerHTML = "";
        }

        const optimizeButton = document.createElement("button");
        optimizeButton.innerText = "Otimizar";
        optimizeButton.classList.add("btn-otimizar", "mt-3");
        optimizeButton.onclick = function() {
            window.location.href = "/result";
        };
        constraintsContainer.appendChild(optimizeButton);
    }

    numFields.addEventListener("change", function() {
        const num = parseInt(numFields.value);
        if (isNaN(num) || num === 0) {
            inputContainer.innerHTML = "";
            objectiveFunction.innerHTML = "";
            constraintsContainer.innerHTML = "";
            return;
        }

        inputContainer.innerHTML = "";
        createObjectiveFunction(num);

        const numConstraints = parseInt(singleNumberField.value);
        if (numConstraints > 0) {
            createConstraints(num, numConstraints);
        } else {
            constraintsContainer.innerHTML = "";
        }
    });

    singleNumberField.addEventListener("change", function() {
        let numVariables = parseInt(numFields.value);
        let numConstraints = parseInt(singleNumberField.value);
        if (numConstraints < 0) {
            singleNumberField.value = 0;
            numConstraints = 0;
            alert("O valor das restrições não pode ser negativo.");
        }

        if (isNaN(numVariables) || isNaN(numConstraints)) return;

        createConstraints(numVariables, numConstraints);
    });
};