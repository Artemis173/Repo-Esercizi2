import React, { useState, useEffect } from 'react';

const Timer1 = () => {
    const [isVisible, setIsVisible] = useState(false);
    
    useEffect(() => {
        const timer = setTimeout(() => {
            setIsVisible(true);
        }, 9000);

        return () => clearTimeout(timer);
    }, []);

    return (
        <div>
            <h1>Timer di codice JSX</h1>
            {isVisible&&<p>Questo è un timer di codice JSX</p>}
        </div>
    );
};

export default Timer1;