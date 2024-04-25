import {useState} from "react";


export const PasswordGenerator = () => {
    const [length, setlength] = useState(8);
    const [includeUppercase, setincludeUppercase] = useState(true);
    const [includeLowercase, setincludeLowercase] = useState(true);
    const [includeNumbers, setincludeNumbers] = useState(true);
    const [includeSymbols, setincludeSymbols] = useState(true);
    const [password, setPassword] = useState("");
    const [backendPassword, setBackendPassword] = useState("");

    const generatePassword = () => {
        let charset = "";
        if (includeUppercase) charset += "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        if (includeLowercase) charset += "abcdefghijklmnopqrstuvwxyz";
        if (includeNumbers) charset += "0123456789";
        if (includeSymbols) charset += "!@#`$%&'()*,-./+=";
    
        let generatedPassword = "";
        for (let i = 0; i < length; i++) {
            const randomIndex = Math.floor(Math.random() * charset.length);
            generatedPassword += charset[randomIndex];
        }
        setPassword(generatedPassword); // Update the state variable
    };

    const copyToClipboard = () => {
        navigator.clipboard.writeText(password);
        alert("Password copied to clipboard");
    };
    return (
    <div className="password-generator">
        <h1 className="main-heading">Strong Password Generator</h1> {/* Main heading */}
        <div className="input-group">
          <label htmlFor="num">Password Length:</label>
          <input type="number" id="num" value={length} onChange={(e)=> setlength(parseInt(e.target.value))} />   
        </div>
        <div className="checkbox-group">
            <input type="checkbox"id="upper" checked={includeUppercase}
            onChange={(e)=>setincludeUppercase(e.target.checked)}/>
            <label htmlFor="upper">include uppercase</label>
        </div>
        <div className="checkbox-group">
            <input type="checkbox"id="lower"checked={includeLowercase} 
            onChange={(e)=>setincludeLowercase(e.target.checked)}/>
            <label htmlFor="lower">include lowercase</label>
        </div>
        <div className="checkbox-group">
            <input type="checkbox"id="numbers" checked={includeNumbers} 
            onChange={(e)=>setincludeNumbers(e.target.checked)}/>
            <label htmlFor="numbers">include numbers</label>
        </div>
        <div className="checkbox-group">
            <input type="checkbox"id="symbol" checked={includeSymbols} 
            onChange={(e)=>setincludeSymbols(e.target.checked)}/>
            <label htmlFor="symbol">include symbol</label>
        </div>
        <button className="generate-btn" onClick={generatePassword}>Generate Password</button>
        <div className="generate-password">
            <input type="text" readOnly value={password} />
            <button className="copy-btn" onClick={copyToClipboard}>Copy</button>
        </div>
    </div>
    );
};